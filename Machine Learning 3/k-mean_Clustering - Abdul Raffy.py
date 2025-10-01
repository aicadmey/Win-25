import numpy as np

class KMeans:
    def __init__(self, n_clusters=2, max_iter=100, tolerance=1e-4):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tolerance = tolerance

    def fit(self, X):
       
        np.random.seed(42)
        initial_indices = np.random.choice(X.shape[0], self.n_clusters, replace=False)
        self.centroids = X[initial_indices]

        for i in range(self.max_iter):
            # clusters based on closest centroid
            self.labels = self._assign_clusters(X)

            # new centroids
            new_centroids = self._compute_centroids(X)

            # convergence
            if np.all(np.abs(new_centroids - self.centroids) < self.tolerance):
                break

            self.centroids = new_centroids

    def _assign_clusters(self, X):
        # distances 
        distances = np.linalg.norm(X[:, None] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)

    def _compute_centroids(self, X):
        # Recompute centroids as the mean of assigned points
        return np.array([X[self.labels == k].mean(axis=0) for k in range(self.n_clusters)])

    def predict(self, X):
        # Prediction of clusters for new data points
        return self._assign_clusters(X)

# Test
if __name__ == "__main__":
    # Sample dataset
    X = np.array([
        [1, 2], [1, 4], [1, 0],
        [10, 2], [10, 4], [10, 0]
    ])

    # Training of KMeans model
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(X)

    # centroids and labels
    print("Centroids:\n", kmeans.centroids)
    print("Labels:", kmeans.labels)

    # Predict for new data
    X_new = np.array([[0, 0], [12, 3]])
    predictions = kmeans.predict(X_new)
    print("Predictions:", predictions)
