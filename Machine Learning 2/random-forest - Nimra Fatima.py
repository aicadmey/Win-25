import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create a Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=10, random_state=42)

# Train the classifier
rf_classifier.fit(X, y)

# Extract an individual decision tree from the Random Forest
individual_tree = rf_classifier.estimators_[0]

# Visualize the decision tree
plt.figure(figsize=(12, 8))
plot_tree(individual_tree, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()