#!/usr/bin/python3
"""Module that contains a function that returns an object
    represented by JSON
"""
import json


def from_json_string(my_str):
    """function that returns an object

    Args:
        my_str: JSON representation
    """
    return json.loads(my_str)
