#!/usr/bin/python3
lookup = __import__('0-lookup').lookup
Rectangle = __import__('9-rectangle').Rectangle

print(lookup(Rectangle))

"""Rectangle = __import__('9-rectangle').Rectangle

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