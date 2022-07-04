#!/usr/bin/python3

class MyList(list):
    """ a class that inherits from list object
    """
    def __init__(self):
        pass

    def print_sorted(self):
        print(sorted(self))
