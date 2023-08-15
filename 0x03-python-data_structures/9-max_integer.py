#!/usr/bin/python3
"""This is a function that finds the biggest integer of a list"""

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    Max = my_list[0]
    for number in my_list:
        if number >= Max:
            Max = number
            return Max
