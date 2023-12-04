#!/usr/bin/python3
def lookup(obj):
    """
    function that returns the list of available attributes
    Args:
        obj: the object to the list
    Returns:
            the list of available attributes and methods of an object.
    """
    return dir(obj)
