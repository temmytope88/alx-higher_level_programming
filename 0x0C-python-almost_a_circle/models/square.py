#!/usr/bin/python3
"""module for a Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class for creating a Square object
        that inherits the Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """A method that intantiates a square object

        Args:
            size (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """it retruns [Square] (<id>) <x>/<y> - <width>/<height>
        """
        value = "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y,
            self.width)
        return value
