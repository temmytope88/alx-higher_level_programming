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
        height = size
        width = size
        super().__init__(width, height, x, y, id=None)

    @property
    def size(self):
        """return the size of a square object

        Returns:
            size: size a square object
        """
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of y

        Args:
            value (int): indicates the y-position of
            a rectangle instance

        Raises:
            TypeError: y should be an integer
            ValueError: y should be >= 0
        """
        self.width = value
        self.height = value

    def __str__(self):
        """it retruns [Square] (<id>) <x>/<y> - <width>/<height>
        """
        value = "[Rectangle] ({}) {}/{} - {}".format(
            self.id, self.x, self.y,
            self.size)
        return value
