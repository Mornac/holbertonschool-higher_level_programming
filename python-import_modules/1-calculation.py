#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
addition = add(a, b)
substraction = sub(a, b)
multiplication = mul(a, b)
division = div(a, b)

print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
