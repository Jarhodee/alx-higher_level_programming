#!/usr/bin/python3

def safe_print_list(my_list=[], y=0):
    nb_element = 0
    for j, element in enumerate(my_list):
        if j < y:
            try:
                print("{}".format(element), end="")
                nb_element += 1
            except BaseException:
                pass
    print("")
    return nb_element