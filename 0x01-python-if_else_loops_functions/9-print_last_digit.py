#!/usr/bin/python3

def print_last_digit(number):
  if number < 0:
    rem = ((-1 * number) % 10)
    return rem
  elif number > 0:
    rem = number % 10
    return rem
  