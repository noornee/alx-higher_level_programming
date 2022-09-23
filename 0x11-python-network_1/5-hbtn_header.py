#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value of the X-Request-Id"""
import sys
import requests

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers.get("X-Request-Id"))
