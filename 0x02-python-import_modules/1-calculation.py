#!/usr/bin/python3
if __name__ == "__main__":
  import calculator_1
  
  a = 10 
  b = 5
  c = calculator_1.add(a, b)
  d = calculator_1.sub(a, b)
  f = calculator_1.mul(a, b)
  e = calculator_1.div(a, b)
  
  print("{} + {} = {}".format(a, b, c))
  print("{} - {} = {}".format(a, b, d))
  print("{} * {} = {}".format(a, b, f))
  print("{} / {} = {}".format(a, b, e))