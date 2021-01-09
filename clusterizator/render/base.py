class RendererBase:
    INITIAL = 'init'
    FINAL = 'final'

    def render(self, dataset, epoch, clusters_ids, centroids):
        self._compute(dataset, epoch, clusters_ids, centroids)
        self._show(epoch)
