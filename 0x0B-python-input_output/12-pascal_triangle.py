#!/usr/bin/python3
""" Module of a function for
pascal triangle """
def pascal_triangle(n):
    """A function that creates pascal triangle

    Args:
        n (str): value on which the pascal triangle
        depends
    """
    list_item = []
    if n <= 0:
        return list_item
    else:
