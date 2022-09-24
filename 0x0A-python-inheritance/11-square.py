#!/usr/bin/python3
""" Module for the square class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class that inherits from
    the class Rectangle

    Args:
        Rectangle (class): create a rectangle
        instance
    """

    def __init__(self, size):
        """instantiate an instance of a square class

        Args:
            size (int): side of a square
        """
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """a function that return determine the
        area of the square

        Returns:
            int: area
        """
        return super().area()

    def __str__(self):
        """return the dimension of the square

        Returns:
            str: [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
