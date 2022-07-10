#!/usr/bin/python3
def no_c(my_string):
  change = my_string.maketrans("c", " ")
  new_string = my_string.translate(change)
  change = new_string.maketrans("C", " ")
  return new_string.translate(change)