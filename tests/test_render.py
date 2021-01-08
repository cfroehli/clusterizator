import numpy as np

from clusterizator.render import TextRenderer, MatPlotRenderer


def test_textrenderer(mocker):
    renderer = TextRenderer()
    print_mock = mocker.patch('builtins.print')
    epoch = np.random.randint(100)
    clusters_ids = np.array([0, 1, 2])
    centroids = np.array([(2, 3), (3, 4)])
    renderer.render(None, epoch, clusters_ids, centroids)
    print_mock.assert_has_calls([
        mocker.call('Epoch {}'.format(epoch)),
        mocker.call('Clusters ids = {}'.format(clusters_ids)),
        mocker.call('Centroids = {}'.format(centroids))
    ])


def test_matplotrenderer(mocker):
    colormap = ['r', 'g', 'b']
    renderer = MatPlotRenderer(colormap)
    plt_title = mocker.patch('matplotlib.pyplot.title')
    plt_scatter = mocker.patch('matplotlib.pyplot.scatter')
    plt_show = mocker.patch('matplotlib.pyplot.show')

    points = np.random.randn(5, 2)
    cluster_ids = np.array([0, 0, 1, 2, 2])
    centroids = np.array([(1, 2), (3, 4), (2, 6)])

    renderer.render(points, 3, cluster_ids, centroids)
    plt_title.assert_called_once_with('Epoch 3')
    data_render_call = plt_scatter.call_args_list[0]
    np.testing.assert_array_equal(points.T, data_render_call[0])
    assert data_render_call[1]['marker'] == '.'
    np.testing.assert_array_equal(renderer._colormap[cluster_ids], data_render_call[1]['color'])
    centroids_render_call = plt_scatter.call_args_list[1]
    np.testing.assert_array_equal(centroids.T, centroids_render_call[0])
    assert centroids_render_call[1] == {'marker': 'x', 'color': 'r'}
    plt_show.assert_called_once_with()
