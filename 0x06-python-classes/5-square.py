#!/usr/bin/python3
""" Square - First python classes's class """


class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def area(self):
        area = self.size ** 2
        return area

    def my_print(self):
        if (self.size == 0):
            print()
        for height in range(self.size):
            for length in range(self.size):
                print("#", end="")
            print()
