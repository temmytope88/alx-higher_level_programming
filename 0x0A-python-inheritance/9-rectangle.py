#!/usr/bin/python3
""" Rectangle class module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A Rectangle class that create a rectangle
    object and inherit from BaseGeometry
    """

    def __init__(self, width, height):

        """ A method that instantiate
        an instance of the Rectangle class

        args: width(int) and height(int)
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ A method that returns area of
        a rectangle

        Returns:
            int: area of a square
        """
        area = self.__width * self.__height
        if area:
            return area
        else:
            return super().area()

    def __str__(self):
        """method that returns the dimension of a
        rectangle

        Returns:
            str: dimension of rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
