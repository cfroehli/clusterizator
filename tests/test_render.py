import numpy as np

from clusterizator.render import TextRenderer, MatPlotRenderer


def test_textrenderer(mocker):
    renderer = TextRenderer()
    print_mock = mocker.patch('builtins.print')
    renderer.render(None, 'EPOCH', [0, 1, 2], [(2, 3), (3, 4)])
    print_mock.assert_has_calls([
        mocker.call('Epoch EPOCH'),
        mocker.call('Clusters ids = [0, 1, 2]'),
        mocker.call('Centroids = [(2, 3), (3, 4)]')
    ])


def test_matplotrenderer(mocker):
    renderer = MatPlotRenderer(['r', 'g', 'b'])
    plt_title = mocker.patch('matplotlib.pyplot.title')
    plt_scatter = mocker.patch('matplotlib.pyplot.scatter')
    plt_show = mocker.patch('matplotlib.pyplot.show')
    renderer.render(np.ones((5, 2)), 3, [0, 0, 1, 2, 2], [(2, 3), (3, 4)])
    plt_title.assert_called_once_with('Epoch 3')
    data_render_call = plt_scatter.call_args_list[0]
    np.testing.assert_array_equal((np.ones((5,)), np.ones((5,))), data_render_call[0])
    assert data_render_call[1]['marker'] == '.'
    np.testing.assert_array_equal(np.array(['r', 'r', 'g', 'b', 'b']), data_render_call[1]['color'])
    centroids_render_calls = plt_scatter.call_args_list[1:]
    assert centroids_render_calls[0] == [(2, 3), {'marker': 'x', 'color': 'r'}]
    assert centroids_render_calls[1] == [(3, 4), {'marker': 'x', 'color': 'r'}]
    plt_show.assert_called_once_with()
