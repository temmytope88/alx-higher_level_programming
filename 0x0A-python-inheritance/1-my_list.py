#!/usr/bin/python3
""" module Mylist """


class MyList(list):
    """ Mylist class that inherits from
    the list class"""

    def print_sorted(self):
        """ a method that prints the list
         in ascending order """

        print(sorted(self))
