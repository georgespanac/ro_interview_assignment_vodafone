import ipaddress
import unittest
from datetime import datetime
import random

from data_structures.entry import Entry
from data_structures.network_collection import NetworkCollection


class NetworkCollectionTestCase(unittest.TestCase):
    def test_remove_invalid_records_one_entry_invalid(self):
        ip1 = ipaddress.ip_network("192.168.1.0/24")
        entry_list1 = [Entry(address="192.0.2.0", last_used=datetime(2021, 11, 4, 0, 0), available=True)]
        network_collection1 = NetworkCollection(ipv4_network=ip1, raw_entry_list=entry_list1)
        network_collection1.remove_invalid_records()
        self.assertEqual(len(network_collection1.entries), 0)

    def test_remove_invalid_records_one_entry_valid(self):
        ip1 = ipaddress.ip_network("0.0.0.0/24")
        entry_list1 = [Entry(address="0.0.0.0", last_used=datetime(2021, 11, 4, 0, 0), available=True)]
        network_collection1 = NetworkCollection(ipv4_network=ip1, raw_entry_list=entry_list1)
        network_collection1.remove_invalid_records()
        self.assertEqual(len(network_collection1.entries), 1)

    def test_remove_invalid_records_multiple_entries(self):
        ip1 = ipaddress.ip_network("192.168.1.0/24")
        entry_list1 = [Entry(address="192.0.2.0", last_used=datetime(2021, 11, 4, 0, 0), available=True)]
        entry_list1 += [Entry(address="192.168.1.0", last_used=datetime(2021, 11, 4, 0, 0), available=True)]
        entry_list1 += [Entry(address="192.168.1.255", last_used=datetime(2021, 11, 4, 0, 0), available=True)]
        entry_list1 += [Entry(address="0.0.0.0", last_used=datetime(2021, 11, 4, 0, 0), available=True)]

        network_collection1 = NetworkCollection(ipv4_network=ip1, raw_entry_list=entry_list1)
        network_collection1.remove_invalid_records()
        self.assertEqual(len(network_collection1.entries), 2)
        self.assertEqual(network_collection1.entries[0].address == "192.168.1.0" or network_collection1.entries[
            1] == "192.168.1.255", True)

    def test_remove_invalid_records_huge_entries_list(self):
        ip1 = ipaddress.ip_network("10.30.12.0/24")
        entry_list1 = []
        entries_size = 100000
        valid_ip = "10.30.12.5"
        for i in range(entries_size):
             entry_list1 += [Entry(address="10.0.2.0", last_used=datetime(2021, 11, 4, 0, 0), available=True)]
             entry_list1 += [Entry(address=valid_ip, last_used=datetime(2021, 11, 4, 0, 0), available=True)]

        network_collection1 = NetworkCollection(ipv4_network=ip1, raw_entry_list=entry_list1)
        network_collection1.remove_invalid_records()
        self.assertEqual(len(network_collection1.entries), entries_size)
        self.assertEqual(network_collection1.entries[0].address == valid_ip, True)

    def test_sort_multiple(self):
        ip1 = ipaddress.ip_network("192.168.1.0/24")
        entry_list1 = [Entry(address="192.168.1.2", last_used=datetime(2021, 11, 4, 0, 0), available=True)]
        entry_list1 += [Entry(address="192.168.1.255", last_used=datetime(2021, 11, 4, 0, 0), available=True)]
        entry_list1 += [Entry(address="192.168.1.0", last_used=datetime(2021, 11, 4, 0, 0), available=True)]
        entry_list1 += [Entry(address="192.168.1.255", last_used=datetime(2021, 11, 4, 0, 0), available=True)]
        entry_list1 += [Entry(address="192.168.1.50", last_used=datetime(2021, 11, 4, 0, 0), available=True)]
        network_collection1 = NetworkCollection(ipv4_network=ip1, raw_entry_list=entry_list1)
        network_collection1.sort_records()
        self.assertEqual(network_collection1.entries[0].address == "192.168.1.0", True)
        self.assertEqual(network_collection1.entries[1].address == "192.168.1.2", True)
        self.assertEqual(network_collection1.entries[2].address == "192.168.1.50", True)
        self.assertEqual(network_collection1.entries[3].address == "192.168.1.255", True)
        self.assertEqual(network_collection1.entries[4].address == "192.168.1.255", True)

    def test_sort_huge_random_generated_entry_list(self):
        ip1 = ipaddress.ip_network("192.168.1.0/24")
        max_ipv4 = 2 ** 32 - 1
        entry_list1 = []
        for i in range(10000):
            random_ip_str = ipaddress.IPv4Address(random.randint(0, max_ipv4))
            entry_list1 += [Entry(address=random_ip_str, last_used=datetime(2021, 11, 4, 0, 0), available=True)]
        network_collection1 = NetworkCollection(ipv4_network=ip1, raw_entry_list=entry_list1)
        network_collection1.sort_records()
        previous_entry = None
        for entry in network_collection1.entries:
            if previous_entry:
                prev_ip_as_int = int(ipaddress.ip_address(previous_entry.address))
                current_ip_as_int = int(ipaddress.ip_address(entry.address))
                self.assertEqual(prev_ip_as_int <= current_ip_as_int, True)
            previous_entry = entry

    def test_sort_single(self):
        ip1 = ipaddress.ip_network("192.168.1.0/24")
        entry_list1 = [Entry(address="192.168.1.2", last_used=datetime(2021, 11, 4, 0, 0), available=True)]
        network_collection1 = NetworkCollection(ipv4_network=ip1, raw_entry_list=entry_list1)
        network_collection1.sort_records()
        self.assertEqual(network_collection1.entries[0].address == "192.168.1.2", True)

    def test_sort_none(self):
        ip1 = ipaddress.ip_network("8.8.8.0/24")
        entry_list1 = []
        network_collection1 = NetworkCollection(ipv4_network=ip1, raw_entry_list=entry_list1)
        network_collection1.sort_records()
        self.assertEqual(len(network_collection1.entries), 0)


if __name__ == '__main__':
    unittest.main()
