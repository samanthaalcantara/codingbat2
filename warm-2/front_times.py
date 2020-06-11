""
Date: 06 07 2020
Author: Samantha Alcantara
Qustion:Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
"""
#Answer
def front_times(str, n):
  if len(str) < 3:
    return str * n
  return str[:3] * n

