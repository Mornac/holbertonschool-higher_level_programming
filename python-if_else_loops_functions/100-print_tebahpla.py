#!/usr/bin/env python3
#!/usr/bin/env python3
result = []
for i in range(25, -1, -1):
    char = chr(97 + i)
    if i % 2 == 0:
        result.append(char.upper())
else:
    result.append(char)
print("".join(result), end="")