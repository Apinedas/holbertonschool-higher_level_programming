#!/usr/bin/python3
"""
    Module with a class MyList to explore inheritance
"""


class MyList(list):
    """
        MyList class: an empty list that inherits the sort method
        from list class.
    """
    def __init__(self):
        self.MyList = []

    def print_sorted(self):
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
