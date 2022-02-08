#!/usr/bin/python3
"""
    Module with base class
"""

import json

class Base():
    """
        Base class for almost a circle
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if (id):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ret = []
        if list_dictionaries:
            for element in list_dictionaries:
                ret.append(element)
        return(json.dumps(ret))

    @classmethod
    def save_to_file(cls, list_objs):
        list_from = []
        with open("{}.json".format(cls.__name__), "w") as file:
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                list_from.append(obj_dict)
            file.write(cls.to_json_string(list_from))

    @staticmethod
    def from_json_string(json_string):
        if (json_string):
            return (json.loads(json_string))
        return ([])

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(cls, **dictionary)
        return (new)

    @classmethod
    def load_from_file(cls):
        ret = []
        with open("{}.json".format(cls.__name__), 'r') as file:
            str_list = file.read()
        dict_list = cls.from_json_string(str_list)
        for obj_dict in dict_list:
            new_obj = cls.create(**obj_dict)
            ret.append(new_obj)
        return(ret)
