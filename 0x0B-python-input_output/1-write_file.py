#!/usr/bin/python3
""" A module for a function that
writes to a text file """


def write_file(filename="", text=""):
    """ A function that writes into a file

    Args:
        filename (str, optional): path of the file. Defaults to ""
        text (str, optional): text to be written to
        the file. Defaults to "".

    Returns:
        int: returns the number of character of the text
        writtn to a file
    """
    with open(filename, "w", encoding="utf-8") as f:
        data = f.write(text)
    return data
