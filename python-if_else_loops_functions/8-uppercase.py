#!/usr/bin/python3
def uppercase(c):
    result = ""
    for char in c:
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
