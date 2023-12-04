#!/usr/bin/python3
'''Module for is_same_class method'''


def is_same_class(obj, a_class):
    """
Compares object type with specified class
Parameters:

        obj: The object that you want to check.
        a_class: The specified class that you want to check against.
Return Value:

        True if obj is an exact instance of the specified class (a_class).
        False if obj is not an exact instance of the specified class.
    """
    return type(obj) is a_class
