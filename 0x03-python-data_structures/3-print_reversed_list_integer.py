#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    else:
        i=0
        while i < len(my_list):
            my_list.reverse()
            print("{:d}".format(my_list[i]))
            i += 1
