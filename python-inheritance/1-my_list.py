#!/usr/bin/python3
"""
Module that defines a class MyList
"""


class MyList(list):
    """
    Class that inherits from the built-in list class
    """
    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        print(sorted(self))
