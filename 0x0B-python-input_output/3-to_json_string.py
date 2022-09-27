#!/usr/bin/python3
"""to_json_string module"""
import json


def to_json_string(my_obj):
    """
        function that returns the JSON representation of an object
        Args:
            my_obj: object input
    """
    return(json.dumps(my_obj))
