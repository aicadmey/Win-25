class RandomForest:
    def __init__(self, n_trees=10, max_depth=None):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.trees = []

    def fit(self, X, y):
        self.trees = []
        for _ in range(self.n_trees):

            indices = '''np.random.choice(len(X), len(X), replace=True)'''
            X_sample = X[indices]
            y_sample = y[indices]


            tree = '''DecisionTree(max_depth=self.max_depth)'''
            tree.fit(X_sample, y_sample)
            self.trees.append(tree)

    def predict(self, X):

        tree_preds = '''np.array([tree.predict(X) for tree in self.trees])'''

        final_preds = '''[np.bincount(tree_preds[:, i]).argmax() for i in range(X.shape[0])]
        return np.array(final_preds)'''
