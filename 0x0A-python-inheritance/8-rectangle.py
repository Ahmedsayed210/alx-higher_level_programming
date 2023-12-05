#!/usr/bin/python3
'''Module for Rectangle class.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''A subclass representing a rectangle.'''
    def __init__(self, width, height):
        '''Constructor.'''
        self.width = width
        self.height = height
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError('width and height must be integers')
        if width <= 0 or height <= 0:
            raise ValueError('width and height must be greater than 0')
