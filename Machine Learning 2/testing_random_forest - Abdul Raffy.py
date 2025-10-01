from sklearn.datasets import make_classification

# Generate a toy dataset
X, y = make_classification(n_samples=100, n_features=5, n_classes=2, random_state=42)

# Train Random Forest
rf = '''RandomForest(n_trees=3, max_depth=3)'''
rf.fit(X, y)

# Predict
predictions = rf.predict(X)
print("Predictions:", predictions)
