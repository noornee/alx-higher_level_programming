#!/usr/bin/python3
"""Module that contains a function that writes an Object to a text file
    Using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an object to a text file

    Args:
        my_obj: object
        filename: filename

    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
