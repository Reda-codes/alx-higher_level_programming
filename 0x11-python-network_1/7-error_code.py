#!/usr/bin/python3
"""Script that sends a request to a URL and displays the response body"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(f"{r.text}")
