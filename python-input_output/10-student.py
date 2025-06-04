#!/usr/bin/python3
"""
Module that defines a Student class
"""


class Student:
    """
    A class representing a student with methods to read and write data.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize the student with first_name, last_name and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dict representation of a student instance
            and writes it to a file.
        """
        if attrs is None:
             return self.__dict__
        else:
            return {key: self.__dict__[key] for key in attrs
                    if key in self.__dict__}
