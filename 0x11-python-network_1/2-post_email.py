#!/usr/bin/python3
"""script that takes a URL and email, sends a POST request to the passed URL"""
from sys import argv
import urllib.request

if __name__ == '__main__':
    par = {"email": argv[2]}
    data = urllib.parse.urlencode(par).encode("ascii")
    with urllib.request.urlopen(argv[1], data) as response:
        print(response.read().decode())
