import random
import numpy as np

class ClusterPoint:
    def __repr__(self):
        return "XY: {} / Cluster: {}".format(self.coordinates, self.cluster)

    @property
    def coordinates(self):
        return self._coordinates

    def __init__(self, coordinates, cluster):
        self._coordinates = coordinates
        self.cluster = cluster

def create_dataset(centers, clusters_size):
    dataset = np.repeat([np.array(c, dtype=float) for c in centers], clusters_size, axis=0)
    dataset += np.random.randn(*dataset.shape)
    return dataset

# Random assign to clusters
def init_points_from_dataset(dataset, n_cluster):
    return [ ClusterPoint(d, np.random.randint(n_cluster)) for d in dataset ]

# Rebuild clusters, if any cluster empty grap a point from another cluster
def rebuild_clusters(points, n_cluster):
    clusters = [ [] for _ in range(n_cluster) ]
    for p in points:
        clusters[p.cluster].append(p.coordinates)
    return clusters

# For each cluster, find the centroid (average points)
def find_centroids(clusters):
    return [ np.mean(c, axis=0) for c in clusters ]

# For each point, check distance to centroids and assign to nearest
def reassign_points_to_nearest_centroids(points, centroids):
    for p in points:
        dist_to_centroids = [ np.linalg.norm(c - p.coordinates) for c in centroids ] #TODO: benchmark ? no squared_norm
        p.cluster = np.argmin(dist_to_centroids)

def clusterize(dataset, n_cluster, max_epochs=10):
    points = init_points_from_dataset(dataset, n_cluster)
    # Repeat until stable or bored
    for _ in range(max_epochs):
        clusters = rebuild_clusters(points, n_cluster)
        centroids = find_centroids(clusters)
        reassign_points_to_nearest_centroids(points, centroids)
    return { 'clusters_ids': [ p.cluster for p in points ], 'clusters_centroids': centroids }

# Fake some data by grouping pts around a few areas
centers = ([6, 4], [-8, -3], [-5, 5])
n_cluster = len(centers)
clusters_size = [4] * n_cluster

# Get some points (more or less grouped in blobs)
dataset = create_dataset(centers, clusters_size)
# Group them to n_cluster clusters
results = clusterize(dataset, n_cluster)
print(results)
