#!/usr/bin/python3
"""a function that retrieves an element from a list like in C programming language."""

def element_at(my_list, dx):
    if dx < 0 or dx > (len(my_list) - 1):
        return None
    return (my_list[dx])
