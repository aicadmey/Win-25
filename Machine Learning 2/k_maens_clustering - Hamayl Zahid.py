import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Step 1: Generate a sample dataset
# For demonstration, we'll create synthetic data using make_blobs
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Step 2: Apply K-means clustering
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

# Get the coordinates of the cluster centers
centroids = kmeans.cluster_centers_

# Step 3: Plot the data points and the cluster centers
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='red', s=200, label="Centroids")

plt.title("K-means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()
