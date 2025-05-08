#!/usr/bin/python3
import sys

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("0 argument.")
    elif len(args) == 1:
        print("1 argument :")
        print("1: {}".format(args[0]))
    else:
        print("{} arguments:".format(len(args)))
        for i, args in enumerate(args, start=1):
            print("{}: {}".format(i, args))

if __name__ == "__main__":
    main()
