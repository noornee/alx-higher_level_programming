#!/usr/bin/python3
"""Module that contains a function that appends
    string at the end of a text file
"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file

    Args:
        filename: filename
        text: text

    Raises:
        pass

    Returns:
        the number of characters added

    """
    with open(filename, "a+") as file:
        return file.write(text)
