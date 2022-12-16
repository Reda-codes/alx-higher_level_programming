#!/usr/bin/python3
import sys import argv
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen(argv[1]) as response:
        data = response.getheader("X-Request-Id")
        print(data)
