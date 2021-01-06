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

# Fake some data by grouping pts around a few areas
centers = ([6, 4], [-8, -3], [-5, 5])
n_cluster = len(centers)
clusters_size = [4] * n_cluster

def create_dataset(centers, clusters_size):
    dataset = np.repeat([np.array(c, dtype=float) for c in centers], clusters_size, axis=0)
    dataset += np.random.randn(*dataset.shape)
    return dataset

dataset = create_dataset(centers, clusters_size)
print(dataset)

# Get some points (more or less grouped in blobs)
# Random assign to clusters
# For each cluster, find the centroid (average points)
# For each point, check distance to centroids and assign to nearest
# Rebuild clusters, if any cluster empty grap a point from another cluster
# Repeat until stable or bored
