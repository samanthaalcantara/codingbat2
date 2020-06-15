"""
Date: 06 12 2020
Author: Samantha Alcantara
Question: The number 6 is a truly great number. 
Given two int values, a and b, return True if 
either one is 6. Or if their sum or difference is 6. 
Note: the function abs(num) computes the absolute value of a number
"""


#Answer

def love6(a, b):
  if (a == b or b == 6):
    return True 
  if (a + b == 6):
    return True
  if(abs(a - b) == 6):
    return True
  return False
