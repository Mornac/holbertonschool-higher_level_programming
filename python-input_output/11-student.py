#!/usr/bin/python3
"""
Module that defines a student class
"""
import os
import sys
__import__('10-student').Student


class Student:
    """
    Class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        return {key: self.__dict__[key] for key in attrs
                if key in self.__dict__}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        with those in the json dictionary.
        Args:
            json (dict): A dictionary containing new values for the attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
