#!/usr/bin/python3
"""This is a function that returns a tuple with the length of a string and its first character"""

def multiple_returns(sentence):
    if len(sentence) == 0:
        return (len(sentence), None)
    else:
        return (len(sentence), sentence[0])
