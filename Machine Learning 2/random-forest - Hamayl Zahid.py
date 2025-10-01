# Import necessary libraries

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Create a synthetic regression dataset
X_reg, y_reg = make_regression(n_samples=100, n_features=1, noise=0.1, random_state=42)

# Split the data into training and testing sets
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.3, random_state=42)

# Create and train the Random Forest Regressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
rf_regressor.fit(X_train_reg, y_train_reg)

# Make predictions on the test set
y_pred_reg = rf_regressor.predict(X_test_reg)

# Evaluate the model performance using Mean Squared Error
mse = mean_squared_error(y_test_reg, y_pred_reg)
print(f'Mean Squared Error of Random Forest Regressor: {mse:.4f}')

# Visualize predicted vs actual values
plt.figure(figsize=(12, 6))
plt.scatter(X_test_reg, y_test_reg, color='blue', label='Actual', alpha=0.6)
plt.scatter(X_test_reg, y_pred_reg, color='red', label='Predicted', alpha=0.6)
plt.title("Random Forest Regressor - Predicted vs Actual Values")
plt.xlabel("Feature")
plt.ylabel("Target Value")
plt.legend()
plt.show()

# Visualize residuals (errors)
residuals = y_test_reg - y_pred_reg
plt.figure(figsize=(12, 6))
plt.scatter(X_test_reg, residuals, color='green', alpha=0.6)
plt.hlines(0, X_test_reg.min(), X_test_reg.max(), colors='red', linewidth=2)
plt.title("Random Forest Regressor - Residuals (Error)")
plt.xlabel("Feature")
plt.ylabel("Residuals (Error)")
plt.show()
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Create a synthetic regression dataset
X_reg, y_reg = make_regression(n_samples=100, n_features=1, noise=0.1, random_state=42)

# Split the data into training and testing sets
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.3, random_state=42)

# Create and train the Random Forest Regressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)
rf_regressor.fit(X_train_reg, y_train_reg)

# Make predictions on the test set
y_pred_reg = rf_regressor.predict(X_test_reg)

# Evaluate the model performance using Mean Squared Error
mse = mean_squared_error(y_test_reg, y_pred_reg)
print(f'Mean Squared Error of Random Forest Regressor: {mse:.4f}')

# Visualize predicted vs actual values
plt.figure(figsize=(12, 6))
plt.scatter(X_test_reg, y_test_reg, color='blue', label='Actual', alpha=0.6)
plt.scatter(X_test_reg, y_pred_reg, color='red', label='Predicted', alpha=0.6)
plt.title("Random Forest Regressor - Predicted vs Actual Values")
plt.xlabel("Feature")
plt.ylabel("Target Value")
plt.legend()
plt.show()

# Visualize residuals (errors)
residuals = y_test_reg - y_pred_reg
plt.figure(figsize=(12, 6))
plt.scatter(X_test_reg, residuals, color='green', alpha=0.6)
plt.hlines(0, X_test_reg.min(), X_test_reg.max(), colors='red', linewidth=2)
plt.title("Random Forest Regressor - Residuals (Error)")
plt.xlabel("Feature")
plt.ylabel("Residuals (Error)")
plt.show()
