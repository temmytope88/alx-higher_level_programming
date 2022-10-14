#!/usr/bin/python3
""" a Node module """


class Node:
    """ Node class """

    @property
    def data(self):
        """ return data vaule """
        return self.__data

    @data.setter
    def data(self, value):
        """ sets data value """
        if isinstance(value, int) is False:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ return next_node value """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ sets next_node value """
        if isinstance(value, Node) is True:
            self.__next_node = value
        else:
            if value is None:
                self.__next_node = None
            else:
                raise TypeError("data must be an integer")

    def __init__(self, data, next_node=None):
        """ Node class constructor """
        self.data = data
        self.next_node = next_node

class SinglyLinkedList:
    """ SinglyLinkedList class constructor """

    def __init__(self):
        self.__head = None


    def sorted_insert(self, value):
        new = Node(value)
        if self.__node is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None \
                and tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new
    def __str__(self):
