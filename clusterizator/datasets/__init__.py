import numpy as np

__all__ = ['create_dataset', 'create_3blobs_dataset']


def create_dataset(centers, clusters_size):
    dataset = np.repeat([np.array(c, dtype=float) for c in centers], clusters_size, axis=0)
    dataset += np.random.randn(*dataset.shape)
    return dataset


def create_3blobs_dataset(clusters_size=8):
    centers = ([6, 4], [-8, -3], [-5, 5])
    n_cluster = len(centers)
    clusters_size = [clusters_size] * n_cluster
    return create_dataset(centers, clusters_size), n_cluster
