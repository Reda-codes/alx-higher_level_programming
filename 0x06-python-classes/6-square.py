#!/usr/bin/python3
"""
This module defines a class Square
"""


class Square:
    """
    a class Square that defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Inits Square with a private instance attribute:
        size and possition.
        """
        self.__size = size
        self.__position = position

    def area(self):
        """
        defines a Public instance method  that
        returns the current square area
        """
        return self.__size*self.__size

    @property
    def size(self):
        """Public instance method getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Public instance method setter"""
        if not type(value) is int:
            print("size must be an integer", end='')
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end='')
            raise ValueError
        self.__size = value

    def my_print(self):
        if (self.__size == 0):
            print("")
        else:
            for i in range(self.position[1]):
                print("")

            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self):
        if type(position) != tuple or \
            len(position) != 2 or \
            not all(isinstance(el, int) for el in position) or \
                not all(el >= 0 for el in position):

            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position
