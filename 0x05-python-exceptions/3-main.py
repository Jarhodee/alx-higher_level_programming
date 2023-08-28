#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

g = 12
h = 2
result = safe_print_division(g, h)
print("{:d} / {:d} = {}".format(g, h, result))

g = 12
h = 0
result = safe_print_division(g, h)
print("{:d} / {:d} = {}".format(g, h, result))

