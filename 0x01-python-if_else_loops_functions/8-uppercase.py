#!/usr/bin/python3

def uppercase(str):
  lists = str.split()
  print(lists)
  for list in lists:
    for apl in list:
      letter = ord(apl)
      if letter in range (65, 91):
        print("{}".format(apl), end = " ")
      elif letter in range (97, 123):
        d = letter + 32 
        print(d)
        print(chr(d),  end = " ")
     
  
uppercase("I am a by of 98")