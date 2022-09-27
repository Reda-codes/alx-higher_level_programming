#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """
        function that read a text file
        Args:
            fileName: name of the file
    """
    with open(filename, encoding="UTF-8") as file:
        var = file.read()
        print(var, end="")
    file.close()
