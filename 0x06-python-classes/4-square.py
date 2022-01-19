#!/usr/bin/python3
""" Square - First python classes's class """


class Square:
    """ Init method for instantiate """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """ Size - Square's size """
        return self._size

    @size.setter
    def size(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    """ Area - Calcs the area of the square """
    def area(self):
        area = self.size ** 2
        return area
