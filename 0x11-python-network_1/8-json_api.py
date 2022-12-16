#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == '__main__':
    if len(argv) < 2 or argv[1].isdigit():
        data = {"q": ""}
        r = requests.post('http://0.0.0.0:5000/search_user', data)
        print("No result")
    else:
        data = {"q": argv[1]}
        r = requests.post('http://0.0.0.0:5000/search_user', data)
        if r.headers['Content-Type'] != 'application/json':
            print("Not a valid JSON")
        else:
            json = r.json()
            print(f"[{json['id']}] {json['name']}")
