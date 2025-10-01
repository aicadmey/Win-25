# example 1
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
print("example 1")
# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2, random_state=42)

# Train a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# example 2
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
print("example 2")
# Load dataset
data = fetch_california_housing()
X, y = data.data, data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2, random_state=42)

# Train a Random Forest regressor
reg = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
reg.fit(X_train, y_train)

# Evaluate
y_pred = reg.predict(X_test)
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")

# example 3
from sklearn.datasets import load_wine
# from sklearn.ensemble import RandomForestClassifier
print("example 3")
# Load dataset
wine = load_wine()
X, y = wine.data, wine.target

# Train a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# Feature importance
for name, importance in zip(wine.feature_names, clf.feature_importances_):
    print(f"{name}: {importance:.4f}")

# example 4
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_digits
print("example 4")
# Load dataset
digits = load_digits()
X, y = digits.data, digits.target

# Define parameter grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 10, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

# Perform Grid Search
grid_search = GridSearchCV(RandomForestClassifier(random_state=42),
                           param_grid, cv=5, scoring='accuracy')
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

# Train Random Forest
clf = RandomForestClassifier(class_weight='balanced', random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
