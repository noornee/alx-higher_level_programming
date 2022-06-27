#!/usr/bin/python3

class Rectangle():
    """
    a Rectangle Class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialize the Rectangle Object
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Return the width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
