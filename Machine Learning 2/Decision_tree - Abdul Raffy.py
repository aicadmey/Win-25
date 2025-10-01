import numpy as np

class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        self.tree = None

    def fit(self, X, y):
        self.tree = self._grow_tree(X, y)

    def predict(self, X):
        return np.array([self._predict(inputs, self.tree) for inputs in X])

    def _grow_tree(self, X, y, depth=0):
        n_samples, n_features = X.shape
        num_labels = len(np.unique(y))


        if depth >= self.max_depth or num_labels == 1 or n_samples == 0:
            leaf_value = self._most_common_label(y)
            return {"leaf": True, "value": leaf_value}

        feature_indices = np.random.choice(n_features, int(np.sqrt(n_features)), replace=False)


        best_feature, best_threshold = self._best_split(X, y, feature_indices)
        if best_feature is None:
            leaf_value = self._most_common_label(y)
            return {"leaf": True, "value": leaf_value}

        left_indices = X[:, best_feature] <= best_threshold
        right_indices = X[:, best_feature] > best_threshold
        left = self._grow_tree(X[left_indices], y[left_indices], depth + 1)
        right = self._grow_tree(X[right_indices], y[right_indices], depth + 1)

        return {"leaf": False, "feature": best_feature, "threshold": best_threshold, "left": left, "right": right}

    def _best_split(self, X, y, feature_indices):
        best_gain = -1
        split_idx, split_thresh = None, None

        for feature in feature_indices:
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                gain = self._information_gain(y, X[:, feature], threshold)
                if gain > best_gain:
                    best_gain = gain
                    split_idx = feature
                    split_thresh = threshold

        return split_idx, split_thresh

    def _information_gain(self, y, X_column, split_thresh):

        parent_entropy = self._entropy(y)


        left_indices = X_column <= split_thresh
        right_indices = X_column > split_thresh

        if len(y[left_indices]) == 0 or len(y[right_indices]) == 0:
            return 0

        n = len(y)
        n_left, n_right = len(y[left_indices]), len(y[right_indices])
        e_left, e_right = self._entropy(y[left_indices]), self._entropy(y[right_indices])
        child_entropy = (n_left / n) * e_left + (n_right / n) * e_right

        return parent_entropy - child_entropy

    def _entropy(self, y):
        hist = np.bincount(y)
        ps = hist / len(y)
        return -np.sum([p * np.log2(p) for p in ps if p > 0])

    def _most_common_label(self, y):
        return np.bincount(y).argmax()

    def _predict(self, inputs, tree):
        if tree["leaf"]:
            return tree["value"]
        feature = tree["feature"]
        if inputs[feature] <= tree["threshold"]:
            return self._predict(inputs, tree["left"])
        return self._predict(inputs, tree["right"])
