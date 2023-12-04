#!/usr/bin/python3
'''Module for inherits_from method.'''


def inherits_from(obj, a_class):
    '''Determines if an object is a true subclass of a class.'''
    return (a_class in obj.__class__.__mro__)
