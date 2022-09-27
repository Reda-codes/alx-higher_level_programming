#!/usr/bin/python3
"""load_from_json_file module"""
import json


def load_from_json_file(filename):
    """
        function that creates an Object from a “JSON file”:
        Args:
            filename: name of the file
    """
    with open(filename) as file:
        data = json.load(file)
    file.close()
    return(data)
