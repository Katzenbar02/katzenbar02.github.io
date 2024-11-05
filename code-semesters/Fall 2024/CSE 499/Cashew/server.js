require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const path = require('path');
const { router: authRouter, authMiddleware } = require('./routes/auth');
const budgetRouter = require('./routes/budget');
const plaid = require('plaid');
const User = require('./models/User');

const app = express();

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

// Connect to MongoDB
const MONGODB_URI = process.env.MONGODB_URI;

mongoose.connect(MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => {
    console.error('Could not connect to MongoDB:', err.message);
    process.exit(1);
});

// Plaid client setup
const plaidClient = new plaid.PlaidApi(
    new plaid.Configuration({
        basePath: plaid.PlaidEnvironments.sandbox, // Change to 'development' or 'production' as needed
        baseOptions: {
            headers: {
                'PLAID-CLIENT-ID': process.env.PLAID_CLIENT_ID,
                'PLAID-SECRET': process.env.PLAID_SECRET,
            },
        },
    })
);

// Routes
app.use('/auth', authRouter);
app.use('/budget', budgetRouter);

// Link Plaid Account
app.post('/plaid/link', authMiddleware, async (req, res) => {
    try {
        const { publicToken } = req.body;
        const response = await plaidClient.itemPublicTokenExchange({
            public_token: publicToken,
        });
        const access_token = response.data.access_token;
        
        // Save the access token for the logged-in user
        const user = await User.findById(req.userId);
        if (!user) {
            return res.status(404).send('User not found');
        }

        user.plaidAccessToken = access_token;
        await user.save();

        res.status(200).send('Plaid account linked successfully');
    } catch (error) {
        res.status(500).send('Error linking Plaid account: ' + error.message);
    }
});

// Create Plaid Link Token
app.post('/plaid/create_link_token', authMiddleware, async (req, res) => {
    try {
        const user = await User.findById(req.userId);
        if (!user) {
            return res.status(404).send('User not found');
        }

        const response = await plaidClient.linkTokenCreate({
            user: {
                client_user_id: user.id,
            },
            client_name: 'Cashew Budgeting App',
            products: ['transactions'],
            country_codes: ['US'],
            language: 'en',
            webhook: 'https://yourapp.com/plaid/webhook', // Optional webhook for updates
        });

        res.json({ link_token: response.data.link_token });
    } catch (error) {
        console.error('Error creating link token:', error);
        res.status(500).send('Error creating link token: ' + error.message);
    }
});

// Fetch transactions from Plaid
app.get('/plaid/transactions', authMiddleware, async (req, res) => {
    try {
        const user = await User.findById(req.userId);
        if (!user || !user.plaidAccessToken) {
            return res.status(404).send('Plaid account not linked');
        }

        // Fetch transactions for the last 30 days
        const startDate = new Date();
        startDate.setDate(startDate.getDate() - 30);
        const endDate = new Date();

        const response = await plaidClient.transactionsGet({
            access_token: user.plaidAccessToken,
            start_date: startDate.toISOString().split('T')[0],
            end_date: endDate.toISOString().split('T')[0],
        });

        res.status(200).json(response.data.transactions);
    } catch (error) {
        res.status(500).send('Error fetching transactions: ' + error.message);
    }
});

// Route for the homepage
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'cashew.html'));
});

// Routes for other pages
app.get('/signup.html', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'signup.html'));
});

app.get('/login.html', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'login.html'));
});

// Protected route for the dashboard
app.get('/dashboard.html', authMiddleware, (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'dashboard.html'));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
