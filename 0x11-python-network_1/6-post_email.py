#!/usr/bin/python3
"""Script sends a POST request to the passed URL with the email parameter"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.post(argv[1], {'email': argv[2]})
    print(r.text)
