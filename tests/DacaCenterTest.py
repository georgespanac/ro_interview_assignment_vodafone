import ipaddress
import unittest
from datetime import datetime

from data_structures.cluster import Cluster
from data_structures.datacenter import Datacenter
from data_structures.entry import Entry
from data_structures.network_collection import NetworkCollection


class DataCenterTestCase(unittest.TestCase):
    def setUp(self):
        ip1 = ipaddress.IPv4Network(address="192.0.2.0")
        entry1 = Entry(address="192.0.2.0", last_used=datetime(2021, 11, 4, 0, 0), available=True)
        entry_list1 = [entry1]
        network_collection1 = NetworkCollection(ipv4_network=ip1, raw_entry_list=entry_list1)
        ip2 = ipaddress.IPv4Network(address="192.0.2.1")
        entry2 = Entry(address="192.0.2.1", last_used=datetime(2022, 11, 4, 0, 0), available=True)
        entry_list2 = [entry2]
        network_collection2 = NetworkCollection(ipv4_network=ip2, raw_entry_list=entry_list2)
        self.network_collection_list1 = [network_collection1]
        self.network_collection_list2 = [network_collection2]

    def test_remove_invalid_clusters_invalid(self):
        cluster1 = Cluster("Datacenter", 1, self.network_collection_list1)
        cluster2 = Cluster("Cluster2", 1, self.network_collection_list2)
        self.cluster_list = [cluster1, cluster2]
        data_center1 = Datacenter("DataCenter1", self.cluster_list)
        data_center1.remove_invalid_clusters()
        self.assertEqual(len(data_center1.cluster_list), 0)

    def test_remove_invalid_clusters_valid1(self):
        cluster1 = Cluster("DAT-1", 1, self.network_collection_list1)
        cluster2 = Cluster("CluserInvalid", 1, self.network_collection_list2)
        self.cluster_list = [cluster1, cluster2]
        data_center1 = Datacenter("DataCenter1", self.cluster_list)
        data_center1.remove_invalid_clusters()
        self.assertEqual(len(data_center1.cluster_list), 1)
        self.assertEqual(data_center1.cluster_list[0].name, "DAT-1")

    def test_remove_invalid_clusters_huge_list(self):
        cluster1 = Cluster("ARA-0", 1, self.network_collection_list1)
        cluster2 = Cluster("XYZ-", 1, self.network_collection_list2)
        size = 100000
        self.cluster_list = [cluster1, cluster2] * size
        data_center1 = Datacenter("aRandodName", self.cluster_list)
        data_center1.remove_invalid_clusters()
        self.assertEqual(len(data_center1.cluster_list), size)

    def test_remove_invalid_clusters_valid2(self):
        cluster1 = Cluster("DAT-12", 1, self.network_collection_list1)
        cluster2 = Cluster("CluserInvalid", 1, self.network_collection_list2)
        self.cluster_list = [cluster1, cluster2]
        data_center1 = Datacenter("DataCenter1", self.cluster_list)
        data_center1.remove_invalid_clusters()
        self.assertEqual(len(data_center1.cluster_list), 1)
        self.assertEqual(data_center1.cluster_list[0].name, "DAT-12")

    def test_remove_invalid_clusters_valid3(self):
        cluster1 = Cluster("DAT-123", 1, self.network_collection_list1)
        cluster2 = Cluster("CluserInvalid", 1, self.network_collection_list2)
        self.cluster_list = [cluster1, cluster2]
        data_center1 = Datacenter("DataCenter1", self.cluster_list)
        data_center1.remove_invalid_clusters()
        self.assertEqual(len(data_center1.cluster_list), 1)
        self.assertEqual(data_center1.cluster_list[0].name, "DAT-123")

    def test_remove_invalid_clusters_valid5(self):
        cluster1 = Cluster("DAT-1234", 1, self.network_collection_list1)
        cluster2 = Cluster("DAT-1", 1, self.network_collection_list1)
        self.cluster_list = [cluster1, cluster2]
        data_center1 = Datacenter("DataCenter1", self.cluster_list)
        data_center1.remove_invalid_clusters()
        self.assertEqual(len(data_center1.cluster_list), 1)
        self.assertEqual(data_center1.cluster_list[0].name, "DAT-1")

    def test_remove_invalid_clusters_invalid2(self):
        cluster1 = Cluster("DAT-", 1, self.network_collection_list1)
        cluster2 = Cluster("CluserInvalid", 1, self.network_collection_list2)
        self.cluster_list = [cluster1, cluster2]
        data_center1 = Datacenter("DataCenter1", self.cluster_list)
        data_center1.remove_invalid_clusters()
        self.assertEqual(len(data_center1.cluster_list), 0)


if __name__ == '__main__':
    unittest.main()
