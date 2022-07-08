#!/usr/bin/python3

for x in range (0, 9):
  for y in range (1, 10):
    if y == 9 and x == 8:
      print("{}{}".format(x,y))
    elif y > x:
      print("{}{}".format(x,y), end = ", ")