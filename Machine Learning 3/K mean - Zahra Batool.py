from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from skimage import io
import numpy as np

# Load and preprocess image
print("example 1")
image = io.imread('https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Red_Apple.jpg/800px-Red_Apple.jpg')
image = image / 255.0  # Normalize
h, w, c = image.shape
pixels = image.reshape(-1, 3)

# Perform K-Means clustering
kmeans = KMeans(n_clusters=8, n_init="auto", random_state=42)
kmeans.fit(pixels)
compressed_pixels = kmeans.cluster_centers_[kmeans.labels_].reshape(h, w, c)

# Display original and compressed images
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(image)
ax[0].set_title("Original Image")
ax[1].imshow(compressed_pixels)
ax[1].set_title("Compressed Image (8 Colors)")
plt.show()

print("example 2")


from sklearn.feature_extraction.text import TfidfVectorizer

# Sample documents
documents = [
    "I love watching football.",
    "Basketball is my favorite sport.",
    "Artificial intelligence is fascinating.",
    "Machine learning is a subset of AI.",
    "I play soccer on weekends."
]

# Convert text to numerical features
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

# Perform K-means clustering
kmeans = KMeans(n_clusters=2,n_init="auto", random_state=0)
kmeans.fit(X)
clusters = kmeans.labels_

# Print cluster assignments
for doc, cluster in zip(documents, clusters):
    print(f"Document: {doc} -> Cluster: {cluster}")

