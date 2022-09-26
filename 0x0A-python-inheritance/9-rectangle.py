#!/usr/bin/python3

""" Rectangle module """

BaseGeo = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeo):
    """ Rectangle class """
    def __init__(self, width, height):
        """ Constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Area function """
        return self.__width * self.__height

    def __str__(self):
        """ string function """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
