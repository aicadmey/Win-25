# example 1
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Example data
emails = [[1, 1], [2, 1], [1, 0], [3, 1], [2, 0]]
labels = [1, 1, 0, 1, 0]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(emails, labels, test_size=0.2,
                                                    random_state=42)

# Logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")

# example 2
from sklearn.datasets import load_iris

# Load dataset
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target,
                                                    test_size=0.2, random_state=42)

# Logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")

# example 3

# Example data
customers = [[2, 1], [5, 0], [1, 1], [8, 0], [4, 1]]
labels = [0, 0, 1, 0, 1]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(customers, labels,
                                                    test_size=0.2, random_state=42)

# Logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")

# example 4

# Example data
patients = [[5, 150], [7, 200], [3, 120], [8, 250], [6, 180]]
labels = [1, 1, 0, 1, 0]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(patients, labels,
                                                    test_size=0.2, random_state=42)

# Logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")

# example 5

# Example data
loans = [[20000, 0], [50000, 1], [15000, 0], [70000, 1], [30000, 0]]
labels = [0, 1, 0, 1, 0]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(loans, labels,
                                                    test_size=0.2, random_state=42)

# Logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")
