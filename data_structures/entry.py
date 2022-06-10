import ipaddress


class Entry:
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """
        self.address = address
        self.available = available
        self.last_used = last_used

    def __lt__(self, other):
        addr_as_int = int(ipaddress.ip_address(self.address))
        other_addr_as_int = int(ipaddress.ip_address(other.address))
        return addr_as_int < other_addr_as_int

    def __eq__(self, other):
        addr_as_int = int(ipaddress.ip_address(self.address))
        other_addr_as_int = int(ipaddress.ip_address(other.address))
        return addr_as_int == other_addr_as_int