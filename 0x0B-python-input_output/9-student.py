#!/usr/bin/python3
""" Module for class (student)
"""


class Student:
    """ A class (student) """
    def __init__(self, first_name, last_name, age):
        """A function that instantiate a class

        Args:
            first_name (str): firstname attribute of a student instance
            last_name (str): last_name attribute of a student instance
            age (int): age attribute of a student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """a method that returns the
        dictionary of the Student class atttibute.
        """
        return self.__dict__
