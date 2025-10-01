# example 1
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
print("example 1")
# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2, random_state=42)

# Train an SVM classifier
clf = SVC(kernel='linear', C=1, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# example 2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles

print("example 2")
# Generate synthetic data
X, y = make_circles(n_samples=300, noise=0.1, factor=0.5, random_state=42)

# Train an SVM with RBF kernel
clf = SVC(kernel='rbf', C=1, gamma=0.5)
clf.fit(X, y)

# Evaluate and visualize
y_pred = clf.predict(X)
print(f"Accuracy: {accuracy_score(y, y_pred) * 100:.2f}%")

# Plot decision boundary
xx, yy = np.meshgrid(np.linspace(X[:, 0].min(), X[:, 0].max(), 500), np.linspace(X[:, 1].min(), X[:, 1].max(), 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
plt.contourf(xx, yy, Z > 0, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor="k")
plt.title("SVM with RBF Kernel")
plt.show()

# example 3
from sklearn.datasets import fetch_california_housing
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
print("example 3")
# Load dataset
data = fetch_california_housing()
X, y = data.data, data.target

# Use only a subset for simplicity
X = X[:, :2]  # Take only 2 features
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2, random_state=42)

# Train an SVR
regressor = SVR(kernel='rbf', C=100, gamma=0.1)
regressor.fit(X_train, y_train)

# Evaluate
y_pred = regressor.predict(X_test)
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")

# example 4
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_digits
print("example 4")
# Load dataset
digits = load_digits()
X, y = digits.data, digits.target

# Define parameter grid
param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf'],
    'gamma': [0.001, 0.01, 0.1, 1]
}

# Perform Grid Search
grid_search = GridSearchCV(SVC(), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X, y)

# Best parameters
print("Best Parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)

# example 5
from sklearn.datasets import make_classification
from sklearn.metrics import classification_report
print("example 5")
# Create imbalanced dataset
X, y = make_classification(
    n_classes=2,
    class_sep=2,
    weights=[0.9, 0.1],
    n_informative=3,
    n_redundant=1,
    flip_y=0,
    n_features=5,
    n_clusters_per_class=1,
    n_samples=1000,
    random_state=42
)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2, random_state=42)

# Train SVM with class weight adjustment
clf = SVC(kernel='rbf', class_weight='balanced', C=1, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

