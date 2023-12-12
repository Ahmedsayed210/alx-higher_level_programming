#!/usr/bin/python3
"""Module to define the Square class."""


from rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class represents a square, inheriting from Rectangle.

    Attributes:
    - id (int): An optional unique identifier for the square.
    - size (int): The size of the square.
    - x (int): The x-coordinate of the square.
    - y (int): The y-coordinate of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Parameters:
        - size (int): The size of the square.
        - x (int, optional): The x-coordinate of the square. Default is 0.
        - y (int, optional): The y-coordinate of the square. Default is 0.
        - id (int, optional): An optional unique identifier for the square.

        If id is provided, it calls the superclass (Rectangle) with the provided id, x, y, width, and height.
        If id is not provided, it generates a unique id using the logic from the Base class.
        The width and height are both set to the value of size.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
     
    @property    
    def size(self):
        '''Getter method for size'''
        return self.width
        
    @size.setter
    def size(self, value):
        '''Setter method for size'''
        self.width = value
        self.height = value
        
        
    def update(self, *args, **kwargs):
        """
        Update the attributes of the square with the provided arguments.

        Args:
        - *args: Positional arguments. If provided, update id, size, x, y in order.
        - **kwargs: Keyword arguments. If provided, update attributes based on key-value pairs.

        If *args exists and is not empty, **kwargs is skipped.
        Each key in **kwargs represents an attribute to the instance.
        """
        atribute = ["id", "size", "x", "y"]

        if args:

            for i in range(len(args)):
                setattr(self, atribute[i], args[i])

        if kwargs:

            for key, value in kwargs.items():

                if key in atribute:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
