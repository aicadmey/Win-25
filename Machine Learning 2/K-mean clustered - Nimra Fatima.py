
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate Euclidean distance
def euclidean_distance(data, centroid):
    return np.sqrt(np.sum((data - centroid) ** 2, axis=1))

# Function to perform K-Means clustering
def kmeans_clustering(data, k, max_iterations=100):
    # Initialize centroids randomly
    centroids = data[np.random.choice(data.shape[0], k, replace=False)]

    for _ in range(max_iterations):
        # Assign each data point to the closest centroid
        distances = np.array([euclidean_distance(data, centroid) for centroid in centroids]).T
        labels = np.argmin(distances, axis=1)

        # Update centroids
        new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])

        # Check for convergence
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return centroids, labels

# Generate random data points
np.random.seed(0)
data = np.random.rand(100, 2)

# Define the number of clusters (K)
k = 5

# Perform K-Means clustering
centroids, labels = kmeans_clustering(data, k)

# Plot the clusters
plt.scatter(data[:, 0], data[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='*', s=200)
plt.show()