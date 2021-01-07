import numpy as np
from clusterizator.lib.cluster_point import ClusterPoint


def test_point():
    coordinates = np.array([3, 7], dtype=float)
    point = ClusterPoint(coordinates, 3)
    assert np.array_equal(point.coordinates, coordinates)
    assert point.cluster == 3
    point.cluster = 2
    assert point.cluster == 2
    assert str(point) == 'XY: [3. 7.] / Cluster: 2'
