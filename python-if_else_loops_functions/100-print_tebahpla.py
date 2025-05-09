#!/usr/bin/python3
result = ""
for i in range(25, -1, -1):
    char = chr(97 + i)
    formatted_char = "{}".format(char.upper() if i % 2 == 0 else char)
    result += formatted_char
print("{}".format(result), end="")
