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

    def to_json(self, attrs=None):
        """a method that returns the
        dictionary of the Student class atttibute.
        """
        if attrs is None:
            value = self.__dict__
        else:
            value = {}
            for item in attrs:
                if item == "first_name":
                    value.update({item: self.first_name})
                if item == "last_name":
                    value.update({item: self.last_name})
                if item == "age":
                    value.update({item: self.age})
        return value

    def reload_from_json(self, json):
        for x, y in json.items():
            if x == "first_name":
                self.first_name = y
            if x == "last_name":
                self.last_name = y
            if x == "age":
                self.age = y
