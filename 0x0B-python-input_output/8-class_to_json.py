#!/usr/bin/python3
"""Module with a function that returns
    the dictionary description with simple data structure
"""


def class_to_json(obj):
    """Function that returns the dictionary desc with simple DS

    Args:
        obj: instance of a Class
    """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
