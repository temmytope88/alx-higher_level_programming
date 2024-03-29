#!/usr/bin/python3
""" recctangle module """


class Rectangle:
    """ class rectangle
    Attributes:
        numnber_of_instance: which increases with every instantiation
        and decreases on deletion of an instance
    """

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ instantition of class rectangle with optional width and height """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ private property, width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if isinstance(value, int) is False:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ private property, height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if isinstance(value, int) is False:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """ area method """
        return self.__height * self.__width

    def perimeter(self):
        """ perimeter method """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """ __str__ method """
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            rec = ""
            for item in range(self.__height - 1):
                value = self.__width * str(self.print_symbol)
                result = value + '\n'
                rec += result
            return rec + self.__width * str(self.print_symbol)

    def __repr__(self):
        """ __repr__ method """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ __del__ method """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
