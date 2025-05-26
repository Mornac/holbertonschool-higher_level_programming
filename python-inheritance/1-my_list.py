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
    def __init__(self, list_instance):
        """
        Initializes the MyList instance
        """
        if not isinstance(list_instance, list):
            raise TypeError("list_instance must be a list")
        if not all(isinstance(i, int) for i in list_instance):
            raise TypeError("list_instance must be a list of integers")
        super().__init__(list_instance)
