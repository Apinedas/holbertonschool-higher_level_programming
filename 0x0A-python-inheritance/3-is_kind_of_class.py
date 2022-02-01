#!/usr/bin/python3
"""
    Module to check if an object is an instance of a class
    of an instance of an inherited class
"""


def is_kind_of_class(obj, a_class):
    """
        is_kind_of_class - Return true if obj is an
        instance of a_class or an inherited class.
    """
    return (isinstance(obj, a_class))
