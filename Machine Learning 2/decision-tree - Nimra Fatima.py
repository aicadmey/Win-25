from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt

# Sample dataset (replace with your actual data)
X = [[3, 1.5], [2, 1], [4, 1.5], [3, 2.5], [2, 2], [2, 3], [1, 2], [1, 3], [1, 1]]
y = ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B',]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=52)

# Create a Decision Tree classifier
classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)

# Train the classifier
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Visualize the decision tree
plt.figure(figsize=(12, 8))
tree.plot_tree(classifier, feature_names=['Feature 1', 'Feature 2'], class_names=['A', 'B'], filled=True)
plt.show()

#Example2:
# Sample dataset (replace with your actual data)
X = [[3, 1.5], [2, 1], [4, 1.5], [3, 2.5], [2, 2], [2, 3], [1, 2], [1, 3], [1, 1]]
y = ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B',]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=32)

# Create a Decision Tree classifier
classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)

# Train the classifier
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Visualize the decision tree
plt.figure(figsize=(12, 8))
tree.plot_tree(classifier, feature_names=['Feature 1', 'Feature 2'], class_names=['A', 'B'], filled=True)
plt.show()

#Example3:
# Sample dataset (replace with your actual data)
X = [[3, 1.5], [2, 1], [4, 1.5], [3, 2.5], [2, 2], [2, 3], [1, 2], [1, 3], [1, 1],[2, 1]]
y = ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B','A']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=52)

# Create a Decision Tree classifier
classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)

# Train the classifier
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Visualize the decision tree
plt.figure(figsize=(12, 8))
tree.plot_tree(classifier, feature_names=['Feature 1', 'Feature 2'], class_names=['A', 'B'], filled=True)
plt.show()

#Example4:
# Sample dataset (replace with your actual data)
X = [[3, 1.5], [2, 1], [4, 1.5], [3, 2.5], [2, 2], [2, 3], [1, 2], [1, 3], [1, 1],[1, 1.5]]
y = ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B','B']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=52)

# Create a Decision Tree classifier
classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)

# Train the classifier
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Visualize the decision tree
plt.figure(figsize=(12, 8))
tree.plot_tree(classifier, feature_names=['Feature 1', 'Feature 2'], class_names=['A', 'B'], filled=True)
plt.show()

#Example5:
# Sample dataset (replace with your actual data)
X = [[3, 1.5], [2, 1], [4, 1.5], [3, 2.5], [2, 2], [2, 3], [1, 2], [1, 3], [1, 1]]
y = ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B',]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=47)

# Create a Decision Tree classifier
classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)

# Train the classifier
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Visualize the decision tree
plt.figure(figsize=(12, 8))
tree.plot_tree(classifier, feature_names=['Feature 1', 'Feature 2'], class_names=['A', 'B'], filled=True)
plt.show()