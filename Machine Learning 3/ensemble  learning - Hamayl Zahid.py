import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_curve, auc

# Generate synthetic dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=15,
                           n_redundant=5, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize individual models
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
gb_model = GradientBoostingClassifier(n_estimators=100, random_state=42)

# Ensemble using VotingClassifier
ensemble_model = VotingClassifier(estimators=[
    ('Random Forest', rf_model),
    ('Gradient Boosting', gb_model)
], voting='soft')

# Train models
rf_model.fit(X_train, y_train)
gb_model.fit(X_train, y_train)
ensemble_model.fit(X_train, y_train)

# Predictions and evaluation
rf_pred = rf_model.predict(X_test)
gb_pred = gb_model.predict(X_test)
ensemble_pred = ensemble_model.predict(X_test)

# Accuracy scores
rf_acc = accuracy_score(y_test, rf_pred)
gb_acc = accuracy_score(y_test, gb_pred)
ensemble_acc = accuracy_score(y_test, ensemble_pred)

print("Random Forest Accuracy:", rf_acc)
print("Gradient Boosting Accuracy:", gb_acc)
print("Ensemble Accuracy:", ensemble_acc)

# Classification report for the ensemble model
print("\nEnsemble Model Classification Report:\n")
print(classification_report(y_test, ensemble_pred))

# ROC Curve and AUC
rf_prob = rf_model.predict_proba(X_test)[:, 1]
gb_prob = gb_model.predict_proba(X_test)[:, 1]
ensemble_prob = ensemble_model.predict_proba(X_test)[:, 1]

rf_fpr, rf_tpr, _ = roc_curve(y_test, rf_prob)
gb_fpr, gb_tpr, _ = roc_curve(y_test, gb_prob)
ensemble_fpr, ensemble_tpr, _ = roc_curve(y_test, ensemble_prob)

rf_auc = auc(rf_fpr, rf_tpr)
gb_auc = auc(gb_fpr, gb_tpr)
ensemble_auc = auc(ensemble_fpr, ensemble_tpr)

# Plot ROC Curves
plt.figure(figsize=(10, 7))
plt.plot(rf_fpr, rf_tpr, label=f'Random Forest (AUC = {rf_auc:.2f})')
plt.plot(gb_fpr, gb_tpr, label=f'Gradient Boosting (AUC = {gb_auc:.2f})')
plt.plot(ensemble_fpr, ensemble_tpr, label=f'Ensemble (AUC = {ensemble_auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--', label='Chance')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.grid()
plt.show()
