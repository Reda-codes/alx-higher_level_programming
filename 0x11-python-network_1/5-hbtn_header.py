#!/usr/bin/python3
"""Script that sends request to the URL and gets the variable X-Request-Id """
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
