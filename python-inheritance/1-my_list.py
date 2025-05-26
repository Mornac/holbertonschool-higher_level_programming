#!/usr/bin/python3
"""
Module that defines a class MyList
"""


class list(list):
    """
    Class that inherits from the built-in list class
    """
    def __init__(self):
        """
        Initializes the MyList instance
        """
        super().__init__()

    def list(self, list_instance):
        """
        Returns the list instance
        """
        list_instance = int(list_instance)
        if isinstance(list_instance, list):
            return list_instance
        else:
            raise TypeError("list_instance must be a list of integers")


class MyList(list):
    """
    Class that inherits from the built-in list class
    """
    def __init__(self):
        """
        Initializes the MyList instance
        """
        super()

    def print_sorted(my_list):
        """
        Function that prints a sorted list
        Args:
        my_list (list): The list to be sorted and printed
        """
        if isinstance(my_list, list):
            print(sorted(my_list))
        else:
            raise TypeError("my_list must be a list")
