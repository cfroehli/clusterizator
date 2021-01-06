class ClusterPoint:
    def __repr__(self):
        return "XY: {} / Cluster: {}".format(self.coordinates, self.cluster)

    @property
    def coordinates(self):
        return self._coordinates

    def __init__(self, coordinates, cluster):
        self._coordinates = coordinates
        self.cluster = cluster
