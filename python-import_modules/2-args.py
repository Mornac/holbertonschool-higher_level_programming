#!/usr/bin/python3
import sys

def main():
    argv = sys.argv[1:]
    if len(argv) == 0:
        print("0 arguments.")
    elif len(argv) == 1:
        print("1 argument :")
        print("1: {}".format(argv[0]))
    else:
        print("{} arguments:".format(len(argv)))
        for i, argv in enumerate(argv, start=1):
            print("{}: {}".format(i, argv))

if __name__ == "__main__":
    main()
