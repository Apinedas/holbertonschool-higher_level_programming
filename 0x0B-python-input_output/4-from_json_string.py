#!/usr/bin/python3
"""
    Module with JSON
"""


def from_json_string(my_str):
    """
        Transform a string to an object using JSON
    """
    import json
    return (json.loads(my_str))
