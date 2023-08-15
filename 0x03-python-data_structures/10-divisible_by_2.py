#!/usr/bin/python3
"""This is a function that finds all multiples of 2 in a list"""

def divisible_by_2(my_list=[]):
    new_list = [True if number % 2 == 0 else False for number in my_list]
    return new_list
