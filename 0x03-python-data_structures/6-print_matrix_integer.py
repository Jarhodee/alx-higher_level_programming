#!/usr/bin/python3
"""This a function that prints a matrix of integers"""

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            print("{:d}".format(i), end=" " if i != row[-1] else "")
            print()
