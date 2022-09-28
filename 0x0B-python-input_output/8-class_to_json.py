#!/usr/bin/python3
""" Module for a function that returns
dictionary format
of a class instance attributes """


def class_to_json(obj):
    """ function that returns dictionary format
    of a class instance attributes

    Args:
        obj (class): object of a class
    """
    data = obj.__dict__
    return data
