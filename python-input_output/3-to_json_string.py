#!/usr/bin/python3
"""
Module that returns the JSON string representation of an object.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON string representation of an object.
    Args:
        my_obj: The object to convert to a JSON string.
    Returns:
        A JSON string representation of the object.
    Raises:
        TypeError: If the object cannot be serialized to JSON.
    """
    return json.dumps(my_obj)
