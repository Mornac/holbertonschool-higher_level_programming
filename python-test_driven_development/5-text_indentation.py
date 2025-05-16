#!/usr/bin/python3

"""
Text Indentation
"""


def text_indentation(text):

    """
    Prints a text with 2 new lines after ".", ",", "?" and ":".
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in ".?:,":
            print(text[i], end="")
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            print(text[i], end="")
            i += 1
