#!/usr/bin/python3
"""Script that sends request to the URL and gets the variable X-Request-Id """
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
