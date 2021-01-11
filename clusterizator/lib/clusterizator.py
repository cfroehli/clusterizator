import numpy as np

from ..render import RendererBase


class Clusterizator:
    def __init__(self, dataset, renderer=None):
        self._dataset = dataset
        self._renderer = renderer

    @property
    def dataset_size(self):
        return self._dataset.shape[0]

    def run(self, n_cluster, max_epochs=10):
        cluster_map = np.random.randint(n_cluster, size=self.dataset_size)

        self._render(RendererBase.INITIAL, cluster_map, centroids=np.empty(shape=(0, 2)))
        for epoch in range(max_epochs):
            centroids = self._update_clusters(cluster_map, n_cluster)
            self._render(epoch, cluster_map, centroids)
            if not self._reassign_points_to_nearest_centroids(cluster_map, centroids):
                break
        self._render(RendererBase.FINAL, cluster_map, centroids)

        return {'clusters_ids': cluster_map, 'clusters_centroids': centroids}

    def _render(self, epoch, cluster_map, centroids):
        if self._renderer:
            self._renderer.render(self._dataset, epoch, cluster_map, centroids)

    def _take_from_another_cluster(self, cluster_to_refill, clusters, cluster_map):
        while True:
            data_index = np.random.randint(self.dataset_size)
            src_cluster_index = cluster_map[data_index]
            src_cluster = clusters[src_cluster_index]
            if src_cluster.size > 1:
                clusters[cluster_to_refill] = np.array([data_index])
                clusters[src_cluster_index] = src_cluster[src_cluster != data_index]
                cluster_map[data_index] = cluster_to_refill
                break

    def _ensure_no_empty_cluster(self, clusters, cluster_map):
        for index, cluster in enumerate(clusters):
            if cluster.size == 0:
                self._take_from_another_cluster(index, clusters, cluster_map)

    def _update_clusters(self, cluster_map, n_cluster):
        clusters = [(cluster_map == cluster_id).nonzero()[0] for cluster_id in range(n_cluster)]
        self._ensure_no_empty_cluster(clusters, cluster_map)
        return np.array([np.mean(self._dataset[c], axis=0) for c in clusters])

    def _reassign_points_to_nearest_centroids(self, cluster_map, centroids):
        reassign_occured = False
        dist_to_centroids = np.linalg.norm(centroids[:, None] - self._dataset, axis=2)
        new_cluster_map = np.argmin(dist_to_centroids, axis=0)
        reassign_occured = np.any(cluster_map != new_cluster_map)
        cluster_map[:] = new_cluster_map
        return reassign_occured
