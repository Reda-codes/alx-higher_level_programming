#!/usr/bin/python3
"""
This module defines a class Square
"""


class Square:
    """
    a class Square that defines a square
    """
    def __init__(self, size=0):
        """Inits Square with a private instance attribute: size."""
        self.__size = size
        if not type(size) is int:
            print("size must be an integer", end='')
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end='')
            raise ValueError

    def area(self):
        """
        defines a Public instance method  that
        returns the current square area
        """
        return self.__size*self.__size
