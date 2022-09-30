#!/usr/bin/python3
""" Module for the Rectangle class"""
from typing import Type
from models.base import Base


class Rectangle(Base):
    """Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for the Rectangle class

        Args:
            width (int): width of the rectangle instance
            height (int): height of the rectangle instance
            x (int, optional): x-axis position. Defaults to 0.
            y (int, optional): y-axis position. Defaults to 0.
            id (_type_, optional): id of the instance. Defaults to None.
        """
        Base.__init__(self, id)

        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        """return the width of a Rectangle object

        Returns:
            width:width of a Rectangle object
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width

        Args:
            value (int): indicates the width of
            a rectangle instance

        Raises:
            TypeError: width should be an integer
            ValueError: width should be > 0
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        else:
            if value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value

    @property
    def height(self):
        """return the height of a Rectangle object

        Returns:
            height:height of a Rectangle object
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height

        Args:
            value (int): indicates the height of
            a rectangle instance

        Raises:
            TypeError: height should be an integer
            ValueError: height should be > 0
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        else:
            if value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value

    @property
    def x(self):
        """return the x-position of a Rectangle object

        Returns:
            x:x-position of a Rectangle object
        """
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x

        Args:
            value (int): indicates the x-position of
            a rectangle instance

        Raises:
            TypeError: x should be an integer
            ValueError: x should be >= 0
        """
        if isinstance(value, int) is False:
            raise TypeError("x must be an integer")
        else:
            if value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value

    @property
    def y(self):
        """return the y-position of a Rectangle object

        Returns:
            y:y-position of a Rectangle object
        """
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y

        Args:
            value (int): indicates the y-position of
            a rectangle instance

        Raises:
            TypeError: y should be an integer
            ValueError: y should be >= 0
        """
        if isinstance(value, int) is False:
            raise TypeError("y must be an integer")
        else:
            if value < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value

    def area(self):
        """ it returns the area of a Rectangle object

        Returns:
            int: Area of a rectangle
        """
        return self.__width * self.__height

    def display(self):
        """ A function that prints the
            image representtion of a rectangle object
        """
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y

        for i in range(y):
            print("")

        for i in range(h):
            print(" " * x, end="")
            print("#" * w)

    def __str__(self):
        """it retruns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        value = "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y,
            self.__width, self.__height)
        return value

    def update(self, *args, **kwargs):
        """ A function that update the attributes of
            a rectangle object
        """
        if args:
            if len(args) == 5:
                self.id = args[0]
                self.height = args[2]
                self.width = args[1]
                self.x = args[3]
                self.y = args[4]

            if len(args) == 4:
                self.id = args[0]
                self.height = args[2]
                self.width = args[1]
                self.x = args[3]

            if len(args) == 3:
                self.id = args[0]
                self.height = args[2]
                self.width = args[1]

            if len(args) == 2:
                self.id = args[0]
                self.width = args[1]

            if len(args) == 1:
                self.id = args[0]

        else:
            for key, value in kwargs.items():
                if key == "width":
                    self.width = value

                if key == "id":
                    self.id = value

                if key == "height":
                    self.height = value

                if key == "x":
                    self.x = value

                if key == "y":
                    self.y = value
