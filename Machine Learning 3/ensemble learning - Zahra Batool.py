from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
print("example 1")
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2, random_state=42)

# Train Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Random Forest Accuracy: {accuracy:.2f}")

print("example 2")
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

# Train AdaBoost
base_model = DecisionTreeClassifier(max_depth=1)  # Weak learner
model = AdaBoostClassifier(base_model, n_estimators=50, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"AdaBoost Accuracy: {accuracy:.2f}")

print("example 3")
from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Define base learners
base_learners = [
    ('lr', LogisticRegression(max_iter=1000)),
    ('svm', SVC(probability=True))
]

# Stacking classifier
stack_model = StackingClassifier(estimators=base_learners,
                                 final_estimator=RandomForestClassifier(random_state=42))
stack_model.fit(X_train, y_train)

# Predict and evaluate
y_pred = stack_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Stacking Ensemble Accuracy: {accuracy:.2f}")

print("example 4")
from sklearn.ensemble import VotingClassifier

# Define base learners
base_learners = [
    ('lr', LogisticRegression(max_iter=1000)),
    ('rf', RandomForestClassifier(random_state=42)),
    ('svm', SVC(probability=True))
]

# Voting classifier
voting_model = VotingClassifier(estimators=base_learners, voting='hard')
voting_model.fit(X_train, y_train)

# Predict and evaluate
y_pred = voting_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Voting Ensemble Accuracy: {accuracy:.2f}")

print("example 5")
from sklearn.ensemble import BaggingClassifier

# Train Bagging Classifier
bagging_model = BaggingClassifier(estimator=DecisionTreeClassifier(),
                                  n_estimators=50, random_state=42)
bagging_model.fit(X_train, y_train)

# Predict and evaluate
y_pred = bagging_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Bagging Classifier Accuracy: {accuracy:.2f}")

