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
