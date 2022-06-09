class Datacenter:
    def __init__(self, name, cluster_list):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """
        self.name = name
        self.cluster_list = cluster_list

    def is_valid_cluster_name(self, cluster_name):
        parts = cluster_name.split('-')
        if len(parts) == 2:
            part1 = parts[0]
            if (part1 and part1 == (self.name[:3]).upper()):
                part2 = parts[1]
                if (part2 and part2.isdigit() and len(part2) in range(1,4)):
                    return True
        return False

    def remove_invalid_clusters(self):
        new_cluster_list = []
        for cluster in self.cluster_list:
            if self.is_valid_cluster_name(cluster.name):
                new_cluster_list += [cluster]
                update = True
        self.cluster_list = new_cluster_list

