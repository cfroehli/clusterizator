import itertools

import numpy as np
import pytest

import clusterizator as Ctor


@pytest.mark.parametrize("cluster_size", [50, 100, 500])
def test_cluster(cluster_size):
    np.random.seed(4)

    dataset = Ctor.create_3blobs_dataset(cluster_size)
    n_cluster = len(dataset['clusters_size'])
    clusterizator = Ctor.Clusterizator(dataset['values'])
    results = clusterizator.run(n_cluster, max_epochs=50)

    ids = results['clusters_ids']
    ids_groups = [len(list(g)) for k, g in itertools.groupby(ids)]
    assert len(ids_groups) == n_cluster
    for group_size in ids_groups:
        assert group_size == cluster_size
