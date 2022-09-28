#!/usr/bin/python3
""" a module for loading and saving objects
in JSON format to a JSON file """

import os
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

list_item = []

filename = "add_item.json"

if os.path.exists(filename):
    data = load_from_json_file(filename)
    list_item = data
    if len(sys.argv) > 1:
        for item in range(1, len(sys.argv)):
            list_item.append(sys.argv[item])
        save_to_json_file(list_item, filename)
    else:
        pass
else:
    if len(sys.argv) > 1:
        for item in range(1, len(sys.argv)):
            list_item.append(sys.argv[item])
        save_to_json_file(list_item, filename)
    else:
        save_to_json_file(list_item, filename)
