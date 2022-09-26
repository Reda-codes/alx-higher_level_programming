#!/usr/bin/python3

""" class Rectangle that inherits from BaseGeometry """

BaseGeo = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeo):
    """ Rectangle class """
    def __init__(self, width, height):
        """ Constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
