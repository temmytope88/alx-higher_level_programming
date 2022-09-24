#!/usr/bin/python3
""" MyInt module """


class MyInt(int):
    """ A class that inherit from the int class

    Args:
        int (class): int class
    """

    def __init__(self, num):
        """initialize num"""
        self.num = num

    def __eq__(self, other):
        """
        Return:
           True if both not equal
        """
        return self.num != other

    def __ne__(self, other):
        """
        Return:
           True if both equal
        """
        return self.num == other
