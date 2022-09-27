#!/usr/bin/python3
"""save_to_json_file module"""
import json


def save_to_json_file(my_obj, filename):
    """
        function that writes an Object to a text file,
        using a JSON representation:
        Args:
            filename: name of the file
            my_obj: obkect input
    """
    with open(filename, "w") as file:
        json.dump(list(my_obj), file)
    file.close()
