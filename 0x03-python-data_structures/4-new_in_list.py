#!/usr/bin/python3
"""This is a function that replaces an element in a list at a specific position"""

def new_in_list(my_list, dx, element):
    new_list = my_list.copy()
    if dx < 0 or dx >= len(my_list):
        return my_list
    new_list[dx] = element
    return new_list
