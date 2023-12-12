#!/usr/bin/python3
'''Module for base method'''


class Base:
    """
    The Base class represents a base object with an optional unique identifier.

    Attributes:
    - id (int): An optional unique identifier for the object.
    - __nb_objects (int): Representing the total number of objects created.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base object.

        Parameters:
        - id (int, optional): An optional unique identifier for the object.
        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
