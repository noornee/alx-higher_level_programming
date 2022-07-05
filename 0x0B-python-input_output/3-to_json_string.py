#!/usr/bin/python3
import json
"""Module that contains a function that returns the
    JSON representation of an object
"""


def to_json_string(my_obj):
    """a function that returns the JSON representation of an object

    Args:
        my_obj: a string obj

    Returns:
        JSON representation of an object
    """
    return json.dumps(my_obj)
