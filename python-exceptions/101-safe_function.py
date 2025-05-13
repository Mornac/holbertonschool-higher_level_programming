#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except:
        return None
    finally:
        print("result of my_div: {}".format(result))
        print("result of print_list: {}".format(result))
        print("{}".format(my_list), end="")
