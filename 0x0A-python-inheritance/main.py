#!/usr/bin/python3
"""lookup = __import__('0-lookup').lookup
Rectangle = __import__('9-rectangle').Rectangle

print(lookup(Rectangle))

Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 9)

print(r)
print(r.area())

Square = __import__('10-square').Square

s = Square(13)

print(s)
print(s.area())

Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())
"""
#with open("0-lookup.py") as f:
#    print(list(f)[len(list(f))-1])

import json


x= {
    "name": "dupe",
    "age": 1,
    "other": ("male", 25, None),
    "sport" : {
        "athletics" : "longjump",
        "ball": "soccer"
        }
    }
print(json.dumps(x))

with open("file.json", "w", encoding="utf-8") as file:
    json.dump(x, file)

with open("file.json", "r", encoding="utf-8") as file:
    print(json.load(file))
