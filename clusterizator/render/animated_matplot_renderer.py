import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

from .base import RendererBase
from .matplot_renderer import MatPlotRenderer


class AniMatPlotRenderer(MatPlotRenderer):
    @property
    def animation(self):
        return self._ani

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._ani = None

    def _compute(self, dataset, epoch, cluster_ids, centroids):
        if epoch == RendererBase.INITIAL:
            self._fig, self._ax = plt.subplots()
            self._frames = []

        title = plt.text(0.5, 1.01, 'Epoch {}'.format(epoch),
                         horizontalalignment='center',
                         verticalalignment='bottom',
                         transform=self._ax.transAxes)
        data = self._ax.scatter(*dataset.T, marker='.', color=self._colormap[cluster_ids])
        centers = self._ax.scatter(*centroids.T, marker='x', color='r')
        self._frames.append([title, data, centers])

    def _show(self, epoch):
        if epoch == RendererBase.FINAL:
            self._ani = ArtistAnimation(self._fig, self._frames, interval=500, repeat_delay=2000, blit=False)
