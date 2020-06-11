"""
Date: 06 01 2020
Author: Samantha Alcantara
Question: Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
"""

#Answer

def front3(str):
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front 

def front3(str):
  if len(str) < 3:
    return str*3
  else:
      return str[:3]*3

