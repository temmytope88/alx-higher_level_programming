#!/usr/bin/python3
""" A square module """


class Square:
    """ a square module """

    def __init__(self, size=0, position=(0, 0)):
        """ intantiation of size of the square """
        self.size = size
        self.position = position

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

    def my_print(self):
        """ method that prints out the square """
        constant = "#"
        value = self.size
        if self.size == 0:
            print()
        else:
            if self.position[0] > 0:
                for i in range(value):
                    print(" " * self.position[0], end="")
                    print(constant * value)
                print()
            else:
                for i in range(value):
                    print(constant * value)
                print()

    @property
    def position(self):
        """ return the position """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the position """
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            if isinstance(value[0], int) is False \
                    or isinstance(value[0], int) is False:
                raise TypeError("position must be a tuple"
                                " of 2 positive integers")
            else:
                if value[0] < 0 or value[1] < 0:
                    raise TypeError("position must be a "
                                    "tuple of 2 positive integers")
                self.__position = value
