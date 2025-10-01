import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample data (replace with your actual data)
X = np.array([[1, 2], [2, 3], [3, 1], [4, 3], [5, 2]])
y = np.array([0, 0, 1, 1, 0])  # 0: class 0, 1: class 1

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Print model coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#Example2:
X = np.array([[1, 2], [2, 3], [3, 1], [4, 3], [5, 2],[6, 2]])
y = np.array([0, 0, 1, 1, 0, 0])  # 0: class 0, 1: class 1

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=52)

# Create and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Print model coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

#Example3:
X = np.array([[1, 2], [2, 3], [3, 1], [4, 3], [5, 2],[6, 2]])
y = np.array([0, 0, 1, 1, 0, 0])  # 0: class 0, 1: class 1

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=60)

# Create and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Print model coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)


#Example4:

X = np.array([[1, 2], [2, 3], [3, 1], [4, 3], [5, 2]])
y = np.array([0, 0, 1, 1, 0])  # 0: class 0, 1: class 1

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=52)

# Create and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Print model coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

#Example5:
X = np.array([[1, 2], [2, 3], [3, 1], [4, 3], [5, 2]])
y = np.array([0, 0, 1, 1, 0])  # 0: class 0, 1: class 1

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=32)

# Create and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Print model coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)