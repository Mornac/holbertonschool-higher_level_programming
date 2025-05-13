#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        elif value != str:
            print("Exception: Unknown format code 'd' for object of type 'str'")
            return False
    except IndexError:
        pass
    return value
