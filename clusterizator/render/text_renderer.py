from .base import RendererBase


class TextRenderer(RendererBase):
    def render(self, dataset, epoch, cluster_ids, centroids):
        print('Epoch {}'.format(epoch))
        print('Clusters ids = {}'.format(cluster_ids))
        print('Centroids = {}'.format(centroids))
