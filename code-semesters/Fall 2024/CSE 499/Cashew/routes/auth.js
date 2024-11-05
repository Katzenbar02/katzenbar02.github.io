// Updated Authentication Routes (auth.js)
const express = require('express');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const User = require('../models/User');
const router = express.Router();

// Secret for JWT
const JWT_SECRET = process.env.JWT_SECRET;

// Signup route
router.post('/signup', async (req, res) => {
    const { name, email, password, confirm_password } = req.body;
    if (password !== confirm_password) {
        return res.status(400).send('Passwords do not match');
    }
    try {
        const user = new User({ name, email, password });
        await user.save();
        res.status(201).send('User registered successfully');
    } catch (error) {
        res.status(400).send('Error registering user: ' + error.message);
    }
});

// Login route
router.post('/login', async (req, res) => {
    const { email, password } = req.body;
    try {
        const user = await User.findOne({ email });
        if (user && (await bcrypt.compare(password, user.password))) {
            const token = jwt.sign({ id: user._id }, JWT_SECRET, { expiresIn: '1h' });
            res.cookie('token', token, { httpOnly: true });
            res.redirect('/dashboard.html');
        } else {
            res.status(400).send('Invalid credentials');
        }
    } catch (error) {
        res.status(400).send('Error logging in: ' + error.message);
    }
});

// Middleware to protect routes
function authMiddleware(req, res, next) {
    const token = req.cookies.token;
    if (token) {
        jwt.verify(token, JWT_SECRET, (err, decoded) => {
            if (err) return res.status(403).send('Unauthorized');
            req.userId = decoded.id;
            next();
        });
    } else {
        res.redirect('/login.html');
    }
}

module.exports = { router, authMiddleware };