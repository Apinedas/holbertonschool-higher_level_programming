#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    key_to_del = None
    for actual_key in a_dictionary:
        if actual_key == key:
            key_to_del = actual_key
    if key_to_del:
        del a_dictionary[key_to_del]
    return a_dictionary
