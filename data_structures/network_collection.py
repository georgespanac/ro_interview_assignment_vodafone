import ipaddress


class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """
        self.ipv4_network = ipv4_network
        self.entries = raw_entry_list

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """
        entries_new = []
        for entry in self.entries:
            if ipaddress.ip_address(entry.address) in self.ipv4_network:
                entries_new += [entry]
        self.entries = entries_new

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """
        self.entries = sorted(self.entries)
