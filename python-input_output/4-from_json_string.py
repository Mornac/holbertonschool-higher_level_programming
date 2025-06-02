#!/usr/bin/python3
"""
Module that returns an object respresented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string
    Args:
        my_str (str): The JSON string to convert
    Returns:
        object: The Python object represented by the JSON string
    """
    object = json.loads(my_str)
    return object
