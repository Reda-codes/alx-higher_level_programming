#!/usr/bin/python3
"""Script that sends a request and displays the body of the response"""
from sys import argv
from urllib import request, error

if __name__ == '__main__':
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode())
    except error.HTTPError as e:
        print(f'Error code: {e.code}')
