import numpy as np

# Get some points (more or less grouped in blobs)
# Random assign to clusters
# For each cluster, find the centroid (average points)
# For each point, check distance to centroids and assign to nearest
# Rebuild clusters, if any cluster empty grap a point from another cluster
# Repeat until stable or bored
