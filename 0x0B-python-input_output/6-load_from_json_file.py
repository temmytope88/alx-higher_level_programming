#!/usr/bin/python3
""" A module for a function
that return the object of a file in
JSON format """
import json


def load_from_json_file(filename):
    """a function
    that return the object of a file in
    JSON format

    Args:
        filename (string): the json file path
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
