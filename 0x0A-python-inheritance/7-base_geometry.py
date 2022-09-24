#!/usr/bin/python3
"""
module for BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry class
    """
    def area(self):
        """a function that raises exception when
            area is not implemented

        Raises:
            Exception: area not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a function that raises an error when
            value is not implemented

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{}" " must be an integer".format(name))
        else:
            if value <= 0:
                raise ValueError("{}"" must be greater than 0".format(name))
