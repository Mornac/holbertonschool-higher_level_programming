#!/usr/bin/python3
"""
Module that adds all arguments to a Python list and saves them to a file.
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    Adds all arguments to a Python list and saves them to a file.
    """
    if len(sys.argv) < 2:
        SystemExit()

    filename = "add_item.json"
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []

    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])

    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    main()
