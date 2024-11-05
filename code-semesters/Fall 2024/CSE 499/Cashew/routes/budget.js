const express = require('express');
const User = require('../models/User');
const authMiddleware = require('./auth').authMiddleware;

const router = express.Router();

// Add or update a budget category for a logged-in user
router.post('/add', authMiddleware, async (req, res) => {
    const { categoryName, categoryLimit } = req.body;

    try {
        const user = await User.findById(req.userId);
        if (!user) {
            return res.status(404).send('User not found');
        }

        // Check if category already exists
        const existingCategory = user.budgets.find(b => b.name === categoryName);
        if (existingCategory) {
            existingCategory.limit = categoryLimit;
        } else {
            user.budgets.push({ name: categoryName, limit: categoryLimit });
        }

        await user.save();
        res.status(200).send('Budget category added/updated successfully');
    } catch (error) {
        res.status(500).send('Error updating budget: ' + error.message);
    }
});

// Get budgets for logged-in user
router.get('/get', authMiddleware, async (req, res) => {
    try {
        const user = await User.findById(req.userId);
        if (!user) {
            return res.status(404).send('User not found');
        }

        res.status(200).json(user.budgets);
    } catch (error) {
        res.status(500).send('Error fetching budgets: ' + error.message);
    }
});

module.exports = router;
