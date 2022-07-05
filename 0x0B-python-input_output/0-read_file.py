#!/usr/bin/python3
""" Module that contains a function that reads
    from a file and print to stdout
"""


def read_file(filename=""):
    """ function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename: filename

    Raises:
        Exception: when file cant be opened
    """

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
