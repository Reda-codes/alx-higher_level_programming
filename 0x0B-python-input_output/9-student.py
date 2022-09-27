#!/usr/bin/python3
"""student module"""


class Student:
    """class Student"""
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        """Init function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        function that retrieves a dictionary 
        representation of a Student instance
        Args:
            obj: object
        """
        return self.__dict__
