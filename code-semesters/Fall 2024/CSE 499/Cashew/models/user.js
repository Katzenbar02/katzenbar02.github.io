const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

const budgetSchema = new mongoose.Schema({
    name: { type: String, required: true },
    limit: { type: Number, required: true },
    spent: { type: Number, default: 0 }
});

const userSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true, unique: true, match: /.+\@.+\..+/ },
    password: { type: String, required: true },
    budgets: [budgetSchema],
    plaidAccessToken: { type: String } // Add this field
});

// Hash the password before saving it
userSchema.pre('save', async function (next) {
    if (!this.isModified('password')) return next();
    this.password = await bcrypt.hash(this.password, 10);
    next();
});

module.exports = mongoose.model('User', userSchema);
