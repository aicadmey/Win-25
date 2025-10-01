# example 1
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
print("example 1")
# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2, random_state=42)

# Train a decision tree classifier
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# Evaluate and visualize
y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# Plot the tree
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=iris.feature_names,
          class_names=iris.target_names, filled=True)
plt.show()

# example 2
from sklearn.datasets import fetch_california_housing
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
print("example 2")
# Load dataset
data = fetch_california_housing()
X, y = data.data, data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2, random_state=42)

# Train a decision tree regressor
regressor = DecisionTreeRegressor(max_depth=5, random_state=42)
regressor.fit(X_train, y_train)

# Evaluate
y_pred = regressor.predict(X_test)
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")

# example 3
from sklearn.datasets import load_wine
print("example 3")
# Load dataset
wine = load_wine()
X, y = wine.data, wine.target

# Train a decision tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)

# Print feature importance
for name, importance in zip(wine.feature_names, clf.feature_importances_):
    print(f"{name}: {importance:.4f}")

# EXAMPLE 4
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
print("example 4")
# Create synthetic dataset
X, y = make_classification(n_features=2, n_classes=2, n_redundant=0, random_state=42)
clf = DecisionTreeClassifier(max_depth=3)
clf.fit(X, y)

# Plot decision boundary
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor="k")
plt.title("Decision Tree Decision Boundary")
plt.show()

# EXAMPLE 5
print("EXAMPLE 5")
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_digits

# Load dataset
digits = load_digits()
X, y = digits.data, digits.target

# Define parameter grid
param_grid = {
    'max_depth': [3, 5, 7, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Perform Grid Search
grid_search = GridSearchCV(DecisionTreeClassifier(random_state=42),
                           param_grid, cv=5, scoring='accuracy')
grid_search.fit(X, y)

# Best parameters
print("Best Parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)

