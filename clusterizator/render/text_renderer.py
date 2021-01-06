from .base import RendererBase


class TextRenderer(RendererBase):
    def render(self, dataset, epoch, cluster_ids, centroids):
        print('Epoch {}'.format(epoch))
        print('Clusters ids = {}'.format(cluster_ids))
        print('Centroids = {}'.format([(c[0], c[1]) for c in centroids]))
