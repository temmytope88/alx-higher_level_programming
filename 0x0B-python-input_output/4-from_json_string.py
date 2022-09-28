#!/usr/bin/python3
""" the module of  a function
that returns the object representation of a JSON """
import json


def from_json_string(my_str):
    """function
    that returns the object representation of a JSON)

    Args:
        my_str (JSON): JSON

    Returns:
        boject: object format of my_str
    """
    return json.loads(my_str)
