#!/usr/bin/python3
""" class_to_json module """


def class_to_json(obj):
    """
        function that returns the dictionary description
        with simple data structure for JSON serialization
        of an object:
        Args:
            obj: object input
    """
    return obj.__dict__
