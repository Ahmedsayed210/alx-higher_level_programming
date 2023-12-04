#!/usr/bin/python3
'''Module for print_sorted method.'''


class Myclass(list):
    '''castom Mylist class'''
    def print_sorted(self):
        '''Method for printing sorted list'''
        print(sorted(self))
