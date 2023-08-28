#!/usr/bin/python3
def safe_print_division(g, h):
    try:
        result = g / h
    except BaseException:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result