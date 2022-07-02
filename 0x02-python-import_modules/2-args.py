#!/usr/bin/python3
import sys

length = len(sys.argv)
if length == 0 or length > 1:
  if length == 0:
    print("{} argumnets".format(length))
  else:
    print("{} arguments".format(length))
    for item in sys.argv:
      position = sys.argv.index(item)
      print("{}: {}".format(position, item))
else:
  print("{} argument".format(length))
  print("1: {}".format(sys.argv[0]))

