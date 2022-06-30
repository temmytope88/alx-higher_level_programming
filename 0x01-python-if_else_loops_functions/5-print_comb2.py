#!/usr/bin/python3

from turtle import ycor


for x in range(0, 10):
    for y in range(0,10):
        if x == 9 and y == 9:
            print("{}{}".format(x,y))
        else:
            print("{}{}, ".format(x,y), end = "")
