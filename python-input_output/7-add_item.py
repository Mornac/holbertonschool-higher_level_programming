#!/usr/bin/python3
"""
Module that adds all arguments to a Python list and saves them to a file.
"""
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def add_item(args, filename='add_item.json'):
    """
    Adds all arguments to a Python list and saves them to a file.
    Args:
        args: The list of arguments to add.
        filename: The name of the file to save the list to.
    """
    if not isinstance(filename, str):
        filename = 'add_item.json'
    save_to_json_file(args, filename)
