#!/usr/bin/python3
"""function that finds a peak"""

def find_peak(list_of_integers):
    """finds a list peak"""
    ln = len(list_of_integers)
    if len(list_of_integers) == 0:
        return
    elif ln == 1:
        return list_of_integers[0]
    elif ln == 2:
        return max(list_of_integers)
    for x in list_of_integers:
