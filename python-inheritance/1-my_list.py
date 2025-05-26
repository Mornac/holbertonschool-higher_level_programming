#!/usr/bin/python3
"""
Module that defines a class MyList
"""


class MyList(list):
    """
    Class that inherits from the built-in list class
    """
    def __init__(self, list_instance=None):
        """
        Initializes the MyList instance
        Args:
        list_instance (list): The list of integers.
        """
        if list_instance is None:
            list_instance = []
        if not isinstance(list_instance, list):
            raise TypeError("list_instance must be a list of integers")
        if not all(isinstance(i, int) for i in list_instance):
            raise TypeError("list_instance must be a list of integers")
        super().__init__(list_instance)

    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        print(sorted(self))
