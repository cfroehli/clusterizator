import numpy as np

__all__ = ['create_dataset', 'create_3blobs_dataset']


def create_dataset(centers, clusters_size):
    values = np.repeat([np.array(c, dtype=float) for c in centers], clusters_size, axis=0)
    values += np.random.randn(*values.shape)
    return {'values': values, 'clusters_size': clusters_size}


def create_3blobs_dataset(clusters_size=8):
    centers = ([6, 4], [-8, -3], [-5, 5])
    clusters_size = [clusters_size] * len(centers)
    return create_dataset(centers, clusters_size)
