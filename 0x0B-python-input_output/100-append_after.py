#!/usr/bin/python3
""" append_after module """


def append_after(filename="", search_string="", new_string=""):
    """
        Function that inserts a line of text to a file,
        after each line containing a specific string
        Args:
            search_string: string to identify
            new_string: string to add
    """
    str = ""

    with open(filename, 'r') as file:
        for line in file:
            str += line
            if search_string in line:
                str += new_string

    with open(filename, 'w') as file:
        file.write(str)
