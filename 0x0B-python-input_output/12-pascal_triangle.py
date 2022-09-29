#!/usr/bin/python3
""" Module of a function for
pascal triangle """


def pascal_triangle(n):
    """A function that creates pascal triangle

    Args:
        n (str): value on which the pascal triangle
        depends
    """
    def factorial(x):
        """A function that determine the factorial of a number

        Args:
            x (int): a number whose factorial is to be found

        Returns:
            int: factorial of a number
        """
        value = 1

        if x == 0:
            value = 1
        else:
            i = x
            while i > 0:
                value = value * i
                i = i - 1
        return value

    list_value = []
    if n <= 0:
        return list_value
    else:
        val_list = []
        for i in range(n):
            if i == 0:
                value = factorial(0)
                inner_list = [value]
                val_list.append(inner_list)
            else:
                p = i + 1
                inner_list = []
                for j in range(p):
                    a = i - j
                    b = j
                    c = i
                    value = factorial(c)/(factorial(b) * factorial(a))
                    inner_list.append(int(value))
                val_list.append(inner_list)
        return val_list
