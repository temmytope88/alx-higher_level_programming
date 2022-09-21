#!/usr/bin/python3
""" A square module """


class Square:
    """ a square module """

    def __init__(self, size=0):
        """ intantiation of size of the square """

        if isinstance(size, int) is True:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size ** 2
