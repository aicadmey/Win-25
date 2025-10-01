import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Data: Hours studied and pass (1 = Yes, 0 = No)
hours_studied = np.array([1, 2, 3, 4, 5, 6, 7]).reshape(-1, 1)
pass_exam = np.array([0, 0, 0, 1, 1, 1, 1])

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(hours_studied, pass_exam, test_size=0.2, random_state=42)

# logistic regression formula
def sigmoid(x, b_0, b_1):
    """Sigmoid function (Logistic function)"""
    return 1 / (1 + np.exp(-(b_0 + b_1 * x)))

# Experiment with different values of b_0 (intercept) and b_1 (coefficient for hours studied)
b_0 = -1  # Intercept
b_1 = 8  # Coefficient for hours studied

# Predicting the probability using the logistic regression formula
predictions_probabilities = sigmoid(X_test, b_0, b_1)

# Predict the class labels based on the probability
predictions = (predictions_probabilities >= 0.5).astype(int)

# Print results
print("Test Set Hours Studied:", X_test.flatten())
print("Predicted Probabilities of Passing:", predictions_probabilities)
print("Predicted Pass/Fail (0 or 1):", predictions)

# Visualizing the results
plt.scatter(hours_studied, pass_exam, color='blue', label='Actual Data')

# Plot the logistic curve with custom b_0 and b_1
x_range = np.linspace(0, 8, 100)  # Range of study hours for plotting the curve
y_range = sigmoid(x_range, b_0, b_1)
plt.plot(x_range, y_range, color='red', label='Logistic Regression Curve')

plt.xlabel('Hours Studied')
plt.ylabel('Probability of Passing')
plt.title('Logistic Regression - Exam Pass Prediction')
plt.legend()
plt.show()
