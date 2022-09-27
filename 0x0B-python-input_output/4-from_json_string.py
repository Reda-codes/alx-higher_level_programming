#!/usr/bin/python3
"""from_json_string module"""
import json


def from_json_string(my_str):
    """
        function that returns an object represented by a JSON string
        Args:
            my_str: json input
    """
    data = json.loads(my_str)
    return(data)
