#!/usr/bin/python3
'''Module for read_file method'''


def read_file(filename=""):
    '''function that reads a text file '''
    with open(filename, encoding="UTF8") as my_file:
        print(myfile.read(), end="")
