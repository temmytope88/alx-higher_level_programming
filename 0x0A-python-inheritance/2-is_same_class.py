#!/usr/bin/python3
""" module of a function """


def is_same_class(obj, a_class):
    """ A function that returns
        true if an object belongs to
        a class
    Args:
        obj (any): an object
        a_class (any): class

    Returns:
        boolean: return True of False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
