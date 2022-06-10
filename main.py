from data_structures.datacenter import Datacenter
from requests.adapters import HTTPAdapter, Retry
import requests

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5):
    session = requests.Session()
    retries = Retry(total=max_retries,
                    backoff_factor=0.1)

    session.mount('http://', HTTPAdapter(max_retries=retries))
    response = session.get(url)
    return response.json()

def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)
    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]


if __name__ == '__main__':
    main()
