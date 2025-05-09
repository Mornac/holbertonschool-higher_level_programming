#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    result = (a, operator, b)

    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    result = operators[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))