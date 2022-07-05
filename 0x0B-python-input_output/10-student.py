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
        obj = self.__dict__.copy()
        if type(attrs) == type(list):
            for i in attrs:
                if type(i) is not str:
                    return obj

            d_list = {}

            for a in range(len(attrs)):
                for b in obj:
                    if attrs[a] == b:
                        d_list[b] = obj[b]
            return d_list

        return obj
