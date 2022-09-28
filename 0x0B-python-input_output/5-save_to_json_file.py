#!/usr/bin/python3
""" A module of a function that
saves an object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """a function that
    saves an object to a file

    Args:
        my_obj (object): object to be saved
        filename (string): path of file
    """


    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)