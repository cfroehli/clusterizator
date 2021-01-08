import numpy as np
import matplotlib.pyplot as plt

from .base import RendererBase


class MatPlotRenderer(RendererBase):
    def __init__(self, colormap):
        super().__init__()
        self._colormap = np.array(colormap)

    def _compute(self, dataset, epoch, clusters_ids, centroids):
        plt.title('Epoch {}'.format(epoch))
        plt.scatter(*dataset.T, marker='.', color=self._colormap[clusters_ids])
        plt.scatter(*centroids.T, marker='x', color='r')

    def _show(self, epoch):
        plt.show()
