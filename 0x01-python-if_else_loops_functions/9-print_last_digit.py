#!/usr/bin/python3

def print_last_digit(number):
  if number < 0:
    rem = ((-1 * number) % 10)
    print(rem, end='')
    return rem
  elif number > 0:
    rem = number % 10
    print(rem, end='')
    return rem
  elif number == 0:
    print(number, end='')
    return number
    
  