import numpy as np
import matplotlib.pyplot as plt

from .base import RendererBase


class MatPlotRenderer(RendererBase):
    def __init__(self, colormap):
        self._colormap = np.array(colormap)
        self._render_initial_state = True
        self._render_intermediate_state = True
        self._render_final_state = True

    def render(self, dataset, epoch, clusters_ids, centroids):
        if not self._render_initial_state and epoch == RendererBase.INITIAL:
            return
        elif not self._render_final_state and epoch == RendererBase.FINAL:
            return
        elif not self._render_intermediate_state:
            return

        plt.title('Epoch {}'.format(epoch))
        plt.scatter(*dataset.T, marker='.', color=self._colormap[clusters_ids])
        for c in centroids:
            plt.scatter(*c, marker='x', color='r')
        plt.show()
