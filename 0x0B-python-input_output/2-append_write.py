#!/usr/bin/python3
"""append_write module"""


def append_write(filename="", text=""):
    """
        function that writes a string to a text file
        Args:
            fileName: name of the file
            text: string input
    """
    with open(filename, mode="a", encoding="UTF-8") as file:
        var = file.write(text)

    file.close()
    return(var)
