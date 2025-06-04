#!/usr/bin/python3
"""
Module that defines a Student class
"""
Student = __import__('9-student').Student


def to_json(self, attrs=None):
    """
    Retrieves a dict representation of a student instance
        and writes it to a file.
    """
    if attrs is None:
        return self.__dict__
    else:
        return {k: v for k, v in self.__dict__.items() if k in attrs}


Student.to_json = to_json
