#!/usr/bin/python3
'''MOdule for Rectangle method.'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A subclass representing a rectangle.'''
    def __init__(self, width, height):
        '''Constructor.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
        - float or int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.width}/{self.height}"

    def __repr__(self):
        """
        Return a detailed representation of the rectangle.

        Returns:
        - str: A string representation containing the width and
        height of the rectangle.
        """
        return f"Rectangle(width={self.width}, height={self.height})"
