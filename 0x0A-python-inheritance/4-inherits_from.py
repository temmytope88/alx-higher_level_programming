#!/usr/bin/python3
""" module of a function """


def inherits_from(obj, a_class):
    """ A function that returns
        true if an object belongs to
        a class and superclass
    Args:
        obj (any): an object
        a_class (any): class

    Returns:
        boolean: return True of False
    """
    if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return True
