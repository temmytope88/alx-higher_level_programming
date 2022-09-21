#!/usr/bin/python3
""" A square module """


class Square:
    """ a square module """

    def __init__(self, size=0):
        """ intantiation of size of the square """
        self.size = size

    @property
    def size(self):
        """ size getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter"""

        if isinstance(value, int) is True:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")


    def area(self):
        """ method that returns the area of the square """
        return self.__size ** 2
