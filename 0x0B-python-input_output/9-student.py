#!/usr/bin/python3
"""Module that defines the class Student
"""


class Student:
    """initialize student class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json"""
        return self.__dict__.copy()
