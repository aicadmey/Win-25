import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


# Function to compute the sigmoid (logistic function)
def sigmoid(x):
    """Sigmoid function for logistic regression."""
    return 1 / (1 + np.exp(-x))


# Custom logistic regression calculation (without using sklearn)
def custom_logistic_regression(X, y, learning_rate=0.1, num_iterations=1000):
    """Custom logistic regression implementation."""
    # Initialize weights and intercept
    m, n = X.shape
    weights = np.zeros(n)  # Initialize weights for n features
    intercept = 0  # Initialize intercept

    # Gradient descent for logistic regression
    for _ in range(num_iterations):
        # Linear combination of inputs and weights
        linear_model = np.dot(X, weights) + intercept

        # Apply the sigmoid function
        y_pred = sigmoid(linear_model)

        # Calculate gradients (derivatives of the cost function)
        dw = (1 / m) * np.dot(X.T, (y_pred - y))
        db = (1 / m) * np.sum(y_pred - y)

        # Update weights and intercept using gradient descent
        weights -= learning_rate * dw
        intercept -= learning_rate * db

    return intercept, weights


# Sample data (binary classification)
# x: independent variable (feature)
# y: dependent variable (binary target)
data_x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)  # Reshaping for sklearn
data_y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Initialize hyperparameters for custom logistic regression
learning_rate = 0.1
num_iterations = 1000

# Run custom logistic regression
intercept, weights = custom_logistic_regression(data_x, data_y, learning_rate, num_iterations)

# Print the estimated coefficients
print(f"Estimated coefficients:\nIntercept (b_0) = {intercept}\nSlope (b_1) = {weights[0]}")

# Make predictions using the custom logistic regression model
predicted_y_prob = sigmoid(np.dot(data_x, weights) + intercept)

# Plotting the results
plt.figure(figsize=(8, 6))

# Plot the actual data points
plt.scatter(data_x, data_y, color="m", marker="o", s=30, label="Actual Data")

# Plot the logistic regression curve
plt.plot(data_x, predicted_y_prob, color="g", label="Fitted Logistic Curve")

# Adding labels and title
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Logistic Regression Curve (Custom Calculations)')

# Display the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
 # 2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


# Function to compute the sigmoid (logistic function)
def sigmoid(x):
    """Sigmoid function for logistic regression."""
    return 1 / (1 + np.exp(-x))


# Custom logistic regression calculation (without using sklearn)
def custom_logistic_regression(X, y, learning_rate=0.1, num_iterations=1000):
    """Custom logistic regression implementation."""
    # Initialize weights and intercept
    m, n = X.shape
    weights = np.zeros(n)  # Initialize weights for n features
    intercept = 0  # Initialize intercept

    # Gradient descent for logistic regression
    for _ in range(num_iterations):
        # Linear combination of inputs and weights
        linear_model = np.dot(X, weights) + intercept

        # Apply the sigmoid function
        y_pred = sigmoid(linear_model)

        # Calculate gradients (derivatives of the cost function)
        dw = (1 / m) * np.dot(X.T, (y_pred - y))
        db = (1 / m) * np.sum(y_pred - y)

        # Update weights and intercept using gradient descent
        weights -= learning_rate * dw + 4
        intercept -= learning_rate * db + 7

    return intercept, weights


# Sample data (binary classification)
# x: independent variable (feature)
# y: dependent variable (binary target)
data_x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)  # Reshaping for sklearn
data_y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Initialize hyperparameters for custom logistic regression
learning_rate = 0.1
num_iterations = 1000

# Run custom logistic regression
intercept, weights = custom_logistic_regression(data_x, data_y, learning_rate, num_iterations)

# Print the estimated coefficients
print(f"Estimated coefficients:\nIntercept (b_0) = {intercept}\nSlope (b_1) = {weights[0]}")

# Make predictions using the custom logistic regression model
predicted_y_prob = sigmoid(np.dot(data_x, weights) + intercept)

# Plotting the results
plt.figure(figsize=(8, 6))

# Plot the actual data points
plt.scatter(data_x, data_y, color="m", marker="o", s=30, label="Actual Data")

# Plot the logistic regression curve
plt.plot(data_x, predicted_y_prob, color="g", label="Fitted Logistic Curve")

# Adding labels and title
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Logistic Regression Curve (Custom Calculations)')

# Display the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
 # 3
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


# Function to compute the sigmoid (logistic function)
def sigmoid(x):
    """Sigmoid function for logistic regression."""
    return 1 / (1 + np.exp(-x))


# Custom logistic regression calculation (without using sklearn)
def custom_logistic_regression(X, y, learning_rate=0.1, num_iterations=1000):
    """Custom logistic regression implementation."""
    # Initialize weights and intercept
    m, n = X.shape
    weights = np.zeros(n)  # Initialize weights for n features
    intercept = 0  # Initialize intercept

    # Gradient descent for logistic regression
    for _ in range(num_iterations):
        # Linear combination of inputs and weights
        linear_model = np.dot(X, weights) + intercept

        # Apply the sigmoid function
        y_pred = sigmoid(linear_model)

        # Calculate gradients (derivatives of the cost function)
        dw = (1 / m) * np.dot(X.T, (y_pred - y))
        db = (1 / m) * np.sum(y_pred - y)

        # Update weights and intercept using gradient descent
        weights -= learning_rate * dw
        intercept -= learning_rate * db

    return intercept, weights


# Sample data (binary classification)
# x: independent variable (feature)
# y: dependent variable (binary target)
data_x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)  # Reshaping for sklearn
data_y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Initialize hyperparameters for custom logistic regression
learning_rate = 0.1
num_iterations = 100

# Run custom logistic regression
intercept, weights = custom_logistic_regression(data_x, data_y, learning_rate, num_iterations)

# Print the estimated coefficients
print(f"Estimated coefficients:\nIntercept (b_0) = {intercept}\nSlope (b_1) = {weights[0]}")

# Make predictions using the custom logistic regression model
predicted_y_prob = sigmoid(np.dot(data_x, weights) + intercept)

# Plotting the results
plt.figure(figsize=(8, 6))

# Plot the actual data points
plt.scatter(data_x, data_y, color="m", marker="o", s=30, label="Actual Data")

# Plot the logistic regression curve
plt.plot(data_x, predicted_y_prob, color="g", label="Fitted Logistic Curve")

# Adding labels and title
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Logistic Regression Curve (Custom Calculations)')

# Display the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
 # 4
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


# Function to compute the sigmoid (logistic function)
def sigmoid(x):
    """Sigmoid function for logistic regression."""
    return 1 / (1 + np.exp(-x))


# Custom logistic regression calculation (without using sklearn)
def custom_logistic_regression(X, y, learning_rate=0.1, num_iterations=1000):
    """Custom logistic regression implementation."""
    # Initialize weights and intercept
    m, n = X.shape
    weights = np.zeros(n)  # Initialize weights for n features
    intercept = 0  # Initialize intercept

    # Gradient descent for logistic regression
    for _ in range(num_iterations):
        # Linear combination of inputs and weights
        linear_model = np.dot(X, weights) + intercept

        # Apply the sigmoid function
        y_pred = sigmoid(linear_model)

        # Calculate gradients (derivatives of the cost function)
        dw = (1 / m) * np.dot(X.T, (y_pred - y)) + 9
        db = (1 / m) * np.sum(y_pred - y) -4

        # Update weights and intercept using gradient descent
        weights -= learning_rate * dw
        intercept -= learning_rate * db

    return intercept, weights


# Sample data (binary classification)
# x: independent variable (feature)
# y: dependent variable (binary target)
data_x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)  # Reshaping for sklearn
data_y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Initialize hyperparameters for custom logistic regression
learning_rate = 0.1
num_iterations = 1000

# Run custom logistic regression
intercept, weights = custom_logistic_regression(data_x, data_y, learning_rate, num_iterations)

# Print the estimated coefficients
print(f"Estimated coefficients:\nIntercept (b_0) = {intercept}\nSlope (b_1) = {weights[0]}")

# Make predictions using the custom logistic regression model
predicted_y_prob = sigmoid(np.dot(data_x, weights) + intercept)

# Plotting the results
plt.figure(figsize=(8, 6))

# Plot the actual data points
plt.scatter(data_x, data_y, color="m", marker="o", s=30, label="Actual Data")

# Plot the logistic regression curve
plt.plot(data_x, predicted_y_prob, color="g", label="Fitted Logistic Curve")

# Adding labels and title
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Logistic Regression Curve (Custom Calculations)')

# Display the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

# 5
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


# Function to compute the sigmoid (logistic function)
def sigmoid(x):
    """Sigmoid function for logistic regression."""
    return 1 / (1 + np.exp(-x))


# Custom logistic regression calculation (without using sklearn)
def custom_logistic_regression(X, y, learning_rate=0.1, num_iterations=1000):
    """Custom logistic regression implementation."""
    # Initialize weights and intercept
    m, n = X.shape
    weights = np.zeros(n)  # Initialize weights for n features
    intercept = 0  # Initialize intercept

    # Gradient descent for logistic regression
    for _ in range(num_iterations):
        # Linear combination of inputs and weights
        linear_model = np.dot(X, weights) + intercept

        # Apply the sigmoid function
        y_pred = sigmoid(linear_model)

        # Calculate gradients (derivatives of the cost function)
        dw = (1 / m) * np.dot(X.T, (y_pred - y)) + 100
        db = (1 / m) * np.sum(y_pred - y) - 100

        # Update weights and intercept using gradient descent
        weights -= learning_rate * dw
        intercept -= learning_rate * db

    return intercept, weights


# Sample data (binary classification)
# x: independent variable (feature)
# y: dependent variable (binary target)
data_x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(-1, 1)  # Reshaping for sklearn
data_y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Initialize hyperparameters for custom logistic regression
learning_rate = 0.1
num_iterations = 1000

# Run custom logistic regression
intercept, weights = custom_logistic_regression(data_x, data_y, learning_rate, num_iterations)

# Print the estimated coefficients
print(f"Estimated coefficients:\nIntercept (b_0) = {intercept}\nSlope (b_1) = {weights[0]}")

# Make predictions using the custom logistic regression model
predicted_y_prob = sigmoid(np.dot(data_x, weights) + intercept)

# Plotting the results
plt.figure(figsize=(8, 6))

# Plot the actual data points
plt.scatter(data_x, data_y, color="m", marker="o", s=30, label="Actual Data")

# Plot the logistic regression curve
plt.plot(data_x, predicted_y_prob, color="g", label="Fitted Logistic Curve")

# Adding labels and title
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Logistic Regression Curve (Custom Calculations)')

# Display the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
