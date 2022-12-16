#!/usr/bin/python3
"""
Python script that takes 2 arguments and
lists 10 last commits of the repository “rails”
"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(f"https://api.github.com/repos/{argv[2]}/{argv[1]}"
                     "/commits")
    data = r.json()
    i = 0
    for key in data:
        if i >= 10:
            break
        print(key.get('sha') + ': ', end="")
        print(key.get('commit').get('author').get('name'))
        i += 1
