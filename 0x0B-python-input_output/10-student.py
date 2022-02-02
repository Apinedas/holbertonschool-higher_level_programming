#!/usr/bin/python3
"""
    Module with student class
"""


class Student():
    """
        Student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (attrs and all(type(attr) is str for attr in attrs)):
            ret_dict = dict()
            for (key, value) in (self.__dict__).items():
                for attr in attrs:
                    if key == attr:
                        ret_dict[key] = value
            return (ret_dict)
        return (self.__dict__)
