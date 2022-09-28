#!/usr/bin/python3
""" the module of  a function
that returns the JSON representation of an object (string) """
import json


def to_json_string(my_obj):
    """function
    that returns the JSON representation of an object (string)

    Args:
        my_obj (string): string

    Returns:
        json: json format of my_obj
    """
    return json.dumps(my_obj)
