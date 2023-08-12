#!/usr/bin/python3

if __name__ == "__main__":
    """Print the list of arguments and numbers."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
        for ix in range(count):
            print("{}: {}".format(ix + 1, sys.argv[ix + 1]))
