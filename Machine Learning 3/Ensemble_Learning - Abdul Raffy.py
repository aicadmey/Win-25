import numpy as np

class DecisionStump:
    def __init__(self):
        self.feature_index = None
        self.threshold = None
        self.polarity = 1
        self.alpha = None

    def fit(self, X, y, sample_weights):
        n_samples, n_features = X.shape
        min_error = float('inf')


        for feature_i in range(n_features):
            feature_values = np.sort(X[:, feature_i])
            thresholds = (feature_values[:-1] + feature_values[1:]) / 2

            for threshold in thresholds:
                for polarity in [1, -1]:
                    predictions = self._make_predictions(X[:, feature_i], threshold, polarity)
                    error = np.sum(sample_weights[y != predictions])


                    if error < min_error:
                        min_error = error
                        self.feature_index = feature_i
                        self.threshold = threshold
                        self.polarity = polarity

    def predict(self, X):
        return self._make_predictions(X[:, self.feature_index], self.threshold, self.polarity)

    def _make_predictions(self, feature_column, threshold, polarity):
        predictions = np.ones(feature_column.shape)
        if polarity == 1:
            predictions[feature_column < threshold] = -1
        else:
            predictions[feature_column > threshold] = -1
        return predictions


class BaggingEnsemble:
    def __init__(self, n_estimators=10):
        self.n_estimators = n_estimators
        self.models = []

    def fit(self, X, y):
        n_samples = X.shape[0]
        for _ in range(self.n_estimators):

            indices = np.random.choice(n_samples, n_samples, replace=True)
            X_sample, y_sample = X[indices], y[indices]

            stump = DecisionStump()
            sample_weights = np.ones_like(y_sample) / n_samples
            stump.fit(X_sample, y_sample, sample_weights)
            self.models.append(stump)

    def predict(self, X):

        predictions = np.array([model.predict(X) for model in self.models])
        return np.sign(np.sum(predictions, axis=0))



if __name__ == "__main__":

    X = np.array([
        [2, 3], [1, 1], [2, 1],
        [5, 6], [6, 6], [6, 7]
    ])
    y = np.array([-1, -1, -1, 1, 1, 1]) 

    ensemble = BaggingEnsemble(n_estimators=5)
    ensemble.fit(X, y)

    # Predictions
    X_test = np.array([[3, 3], [4, 5]])
    predictions = ensemble.predict(X_test)
    print("Predictions:", predictions)
