"""
Date: 06 01 2020
Author: Samantha Alcantara
Question: Given a string, return a new string where the first and last chars have been exchanged.
"""

#Answer

def front_back(str):
  if len(str) == 1:
    return str
  if len(str) == 2:
    return str [1] + str [0] 
  else:
    return str [-1:] + str [1:-1] + str [:1]
 
