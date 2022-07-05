#!/usr/bin/python3
"""Module that contains a function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """function that writes a string to a text filename

    Args:
        filename: filename
        text: text

    Raises:
        pass

    Returns:
        the number of characters written
    """

    with open(filename, 'w+') as file:
        return file.write(text)
