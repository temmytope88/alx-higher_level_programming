#!/usr/bin/python3
# class
class Rectangle:

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError('width must be an integer')
        elif not isinstance(value, int):
            raise TypeError('width must be an integer')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError('height must be an integer')
        elif not isinstance(value, int):
            raise TypeError('height must be an integer')
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
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
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) and isinstance(rect_2, Rectangle):
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2
        else:
            if not isinstance(rect_1, Rectangle):
                raise TypeError("rect_1 must be an instance of Rectangle")
            if not isinstance(rect_2, Rectangle()):
                raise TypeError("rect_2 must be an instance of Rectangle")
