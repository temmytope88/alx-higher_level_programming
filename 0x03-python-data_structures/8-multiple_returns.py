#!/usr/bin/python3
def multiple_returns(sentence):
  count = len(sentence)
  if count == 0:
    char = "none"
  else:
    char = sentence[0]
  return count, char