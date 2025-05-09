#!/usr/bin/python3
result = ""
for i in range(25, -1, -1):
    char = chr(97 + i)
    if i % 2 == 0:
        result += char.upper()
    else:
        result += char
print(result, end="")