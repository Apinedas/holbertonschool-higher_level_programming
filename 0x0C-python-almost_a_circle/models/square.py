#!/usr/bin/python3
"""
    Module with the Square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square class from Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
                .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return (self.__width)

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
            self.__height = value

    def update(self, *args, **kwargs):
        """
            Updates the instance with args
            and kwargs
        """
        if (args or (args and kwargs)):
            if (len(args) >= 1):
                self.id = args[0]
            if (len(args) >= 2):
                self.size = args[1]
            if (len(args) >= 3):
                self.x = args[2]
            if (len(args) >= 4):
                self.y = args[3]
        if (kwargs):
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
            Returns the dictionary instance's representation
        """
        return ({'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y})
