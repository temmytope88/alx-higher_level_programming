#!/usr/bin/python3
""" A module for reading text file
"""


def read_file(filename=""):
    """ A function that reads a text file

    Args:
        filename (str, optional): _description_. Defaults to "".
    """

    with open(filename, encoding="utf-8") as f:
        data = f.read()
    print(data, end="")
