from sklearn.tree import DecisionTreeClassifier

# Example dataset
dataset = [
    (40000, 0.2, 'low'),
    (60000, 0.8, 'low'),
    (80000, 0.6, 'moderate'),
    (20000, 0.1, 'high'),
    (30000, 0.3, 'moderate'),
    (90000, 0.7, 'high'),
    (70000, 0.5, 'low')
]

# Extracting features and labels from the dataset
features = [(income, credit_score) for income, credit_score, _ in dataset]
labels = [risk_label for _, _, risk_label in dataset]

# Creating and training the decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(features, labels)

# New applicants to assess
new_applicant1 = (45000, 0.7)
new_applicant2 = (75000, 0.2)
new_applicant3 = (25000, 0.5)

# Predicting the risk level for the new applicants
risk_prediction1 = clf.predict([new_applicant1])
risk_prediction2 = clf.predict([new_applicant2])
risk_prediction3 = clf.predict([new_applicant3])

# Mapping the prediction to risk labels
risk_mapping = {'low': 'Low Risk', 'moderate': 'Moderate Risk', 'high': 'High Risk'}
# Mapping the predictions to risk labels
predicted_risk_level1 = risk_mapping[risk_prediction1[0]]
predicted_risk_level2 = risk_mapping[risk_prediction2[0]]
predicted_risk_level3 = risk_mapping[risk_prediction3[0]]

# Printing the predicted risk levels for the new applicants
print("Predicted Risk Level for Applicant 1:", predicted_risk_level1)
print("Predicted Risk Level for Applicant 2:", predicted_risk_level2)
print("Predicted Risk Level for Applicant 3:", predicted_risk_level3)
