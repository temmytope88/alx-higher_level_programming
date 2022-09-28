#!/usr/bin/python3
""" Module for BaseModel class """


class Base:
    """BaseModel Class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Construtor for the BaseModel class

        Args:
            id (int, optional): Model instant id
        """
        Base.__nb_objects +=1
        if id is None:
            self.id = Base.__nb_objects
        else:
            self.id = id
