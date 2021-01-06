import itertools
import pytest

import numpy as np

from clusterizator import *

def test_cluster():
    np.random.seed(3)
    cluster_size = 200
    dataset, n_cluster = create_3blobs_dataset(cluster_size)
    clusterizator = Clusterizator(dataset)
    results = clusterizator.run(n_cluster, max_epochs=50)
    ids = results['clusters_ids']
    ids_groups = [ len(list(g)) for k, g in itertools.groupby(ids) ]
    assert len(ids_groups) == n_cluster
    for group_size in ids_groups:
        assert group_size == cluster_size
