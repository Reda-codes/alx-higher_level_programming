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

    def to_json(self, attrs=None):
        """
            Function retrieves a dictionary representation
            of a Student instance
        """
        json = {}

        if None is attrs:
            return self.__dict__

        for attr in attrs:
            if type(attr) is not str:
                continue
            if hasattr(self, attr):
                json[attr] = getattr(self, attr)

        return json

    def reload_from_json(self, json):
        """
            Function replaces all attributes of the Student instance
        """
        for key in json.keys():
            self.__dict__[key] = json[key]
