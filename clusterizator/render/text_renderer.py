from .base import RendererBase


class TextRenderer(RendererBase):
    def __init__(self, only_results=True):
        self._only_results = only_results

    def render(self, dataset, epoch, cluster_ids, centroids):
        if self._only_results and epoch != RendererBase.FINAL:
            return

        print('Epoch {}'.format(epoch))
        print('Clusters ids = {}'.format(cluster_ids))
        print('Centroids = {}'.format(centroids))
