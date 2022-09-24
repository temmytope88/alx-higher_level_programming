#!/usr/bin/python3
""" module of a function """


def is_kind_of_class(obj, a_class):
    """ A function that returns
        true if an object belongs to
        a class and superclass
    Args:
        obj (any): an object
        a_class (any): class

    Returns:
        boolean: return True of False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
