#!/usr/bin/python3
"""
    Module with rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """
        Rectangle class inherit from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
            Return rectangle's area
        """
        return (self.width * self.height)

    def display(self):
        """
            Displays the rectangle using # character
            taking x and y into account
        """
        for k in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
            Updates the instance with args
            and kwargs
        """
        if (args):
            if (len(args) >= 1):
                self.id = args[0]
            if (len(args) >= 2):
                self.width = args[1]
            if (len(args) >= 3):
                self.height = args[2]
            if (len(args) >= 4):
                self.x = args[3]
            if (len(args) >= 5):
                self.y = args[4]
        elif (kwargs):
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
            Returns the class dictionary
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
