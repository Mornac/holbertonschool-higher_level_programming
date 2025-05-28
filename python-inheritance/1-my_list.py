#!/usr/bin/python3
"""
Module that defines a class MyList
"""


class MyList(list):
    """
    Class that inherits from the built-in list class
    """

    def append(self, object):
        if type(object) is not int:
            raise TypeError("my_list must be a list of integers")
        super().append(object)

    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        print(sorted(self))
