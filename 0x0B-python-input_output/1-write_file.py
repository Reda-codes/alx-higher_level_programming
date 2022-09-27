#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    """
        function that writes a string to a text file
        Args:
            fileName: name of the file
            text: string input
    """
    num = 0
    with open(filename, mode="w", encoding="UTF-8") as file:
        var = file.write(text)

    file.close()
    return(var)
