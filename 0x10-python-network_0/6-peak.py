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

    m = int(ln / 2)
    p = list_of_integers[m]
    if p > list_of_integers[m - 1] and p > list_of_integers[m + 1]:
        return p
    elif p < list_of_integers[m - 1]:
        return find_peak(list_of_integers[:m])
    else:
        return find_peak(list_of_integers[m + 1:])
