#!/usr/bin/python3
"""
Module that returns the dictionary description with simple data structure
for JSON serialization of an object.
"""
import json


class MyClass:
    """
    Example class to demonstrate serialization.
    """
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"MyClass(name={self.name}, value={self.value})"


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.
    Args:
        obj: The object to serialize
    Returns:
        dict: The dictionary representation of the object
    """
    return obj.__dict__ if hasattr(obj, "__dict__") else obj
