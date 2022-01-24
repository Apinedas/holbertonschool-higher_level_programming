#!/usr/bin/python3
"""Module for Rectangle class
"""


class Rectangle:
    """This class describes a rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Rectangle's width (int) """
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Rectangle's height (int) """
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ Instance method to calc Rectangle's area """
    def area(self):
        return (self.width * self.height)

    """ Instance method to calc Rectangle's perimeter """
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return (0)
        return ((2 * self.width) + (2 * self.height))

    """ __str__ method to print the Rectangle """
    def __str__(self):
        ret = ""
        if self.height == 0 or self.width == 0:
            return (ret)
        for i in range(self.height):
            for j in range(self.width):
                ret += "#"
            ret += "\n"
        ret = ret[0:-1]
        return (ret)

    """ __repr__ method to recreate the Rectangle """
    def __repr__(self):
        return ("Rectangle(" + str(self.width) + ", " + str(self.height) + ")")

    """ __del__ method to print a message when
    an instance is deleted """
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
