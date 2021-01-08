class RendererBase:
    INITIAL = 'init'
    FINAL = 'final'

    def __init__(self):
        self._render_initial_state = True
        self._render_intermediate_state = True
        self._render_final_state = True

    def _compute(self, dataset, epoch, clusters_ids, centroids):
        raise NotImplementedError()

    def _show(self, epoch):
        raise NotImplementedError()

    def render(self, dataset, epoch, clusters_ids, centroids):
        if not self._render_initial_state and epoch == RendererBase.INITIAL:
            return
        elif not self._render_final_state and epoch == RendererBase.FINAL:
            return
        elif not self._render_intermediate_state:
            return

        self._compute(dataset, epoch, clusters_ids, centroids)
        self._show(epoch)
