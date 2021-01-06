import random

import numpy as np

from ..render import RendererBase
from .cluster_point import ClusterPoint

class Clusterizator:
    def __init__(self, dataset, renderer=None):
        self._dataset = dataset
        self._renderer = renderer

    def run(self, n_cluster, max_epochs=10):
        points = self._init_points_from_dataset(n_cluster)
        self._render(points, centroids=[], epoch=RendererBase.INITIAL)
        for epoch in range(max_epochs):
            clusters = Clusterizator._rebuild_clusters(points, n_cluster)
            centroids = Clusterizator._find_centroids(clusters)
            if not Clusterizator._reassign_points_to_nearest_centroids(points, centroids):
                break
            self._render(points, centroids, epoch)
        self._render(points, centroids, epoch=RendererBase.FINAL)

        return { 'clusters_ids': Clusterizator.cluster_ids(points), 'clusters_centroids': centroids }

    def _init_points_from_dataset(self, n_cluster):
        return [ ClusterPoint(d, np.random.randint(n_cluster)) for d in self._dataset ]

    def _render(self, points, centroids, epoch):
        if self._renderer:
            self._renderer.render(self._dataset, epoch, Clusterizator.cluster_ids(points), centroids)

    @staticmethod
    def cluster_ids(points):
        return [ p.cluster for p in points ]

    @staticmethod
    def _ensure_no_empty_cluster(clusters, points):
        for i, c in enumerate(clusters):
            if not c:
                while True:
                    p = random.choice(points)
                    source_cluster = clusters[p.cluster]
                    if len(source_cluster) > 1:
                        for s_i, s_coordinates in enumerate(source_cluster):
                            if np.array_equal(p.coordinates, s_coordinates):
                                del source_cluster[s_i]
                                break
                        p.cluster = i
                        c.append(p.coordinates)
                        break

    @staticmethod
    def _rebuild_clusters(points, n_cluster):
        clusters = [ [] for _ in range(n_cluster) ]
        for p in points:
            clusters[p.cluster].append(p.coordinates)

        Clusterizator._ensure_no_empty_cluster(clusters, points)
        return clusters

    @staticmethod
    def _find_centroids(clusters):
        return [ np.mean(c, axis=0) for c in clusters ]

    @staticmethod
    def _reassign_points_to_nearest_centroids(points, centroids):
        reassign_occured = False
        for i, p in enumerate(points):
            dist_to_centroids = [ np.linalg.norm(c - p.coordinates) for c in centroids ]
            new_cluster = np.argmin(dist_to_centroids)
            reassign_occured |= new_cluster != p.cluster
            p.cluster = new_cluster
        return reassign_occured
