#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value of the X-Request-Id"""
import sys
from urllib.request import urlopen

if __name__ == "__main__":
    url = sys.argv[1]
    with urlopen(url) as response:
        for data in response.getheaders():
            if data[0] == "X-Request-Id":
                print(data[1])
