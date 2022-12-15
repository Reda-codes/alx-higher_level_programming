#!/usr/bin/python3
"""function that finds a peak"""

def find_peak(list_of_integers):
    """finds a list peak"""
    if len(list_of_integers) == 0:
        return
    return max(list_of_integers)
