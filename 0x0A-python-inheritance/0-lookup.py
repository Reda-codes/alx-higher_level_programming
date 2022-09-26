#!/usr/bin/python3
"""
function that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Args:
        obj (Any): object
    Returns:
        list of attributes and methods
    """
    return dir(obj)
