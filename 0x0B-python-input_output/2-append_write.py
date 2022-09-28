#!/usr/bin/python3
""" Module for the funtion that
appends to a text file
"""


def append_write(filename="", text=""):
    """A function that appends to a file

    Args:
        filename (str, optional): path of the file. Defaults to "".
        text (str, optional): text to be appended. Defaults to "".

    Returns:
        int: number of the characters of the text
        appended to the file
    """
    with open(filename, "a", encoding="utf-8") as f:
        data = f.write(text)
    return data
