#!/usr/bin/python3
'''Module for read_file method'''


def read_file(filename=""):
    '''Print the contents of a UTF8 text file to stdout.'''
    with open(filename, encoding="UTF8") as my_file:
        print(myfile.read(), end="")
