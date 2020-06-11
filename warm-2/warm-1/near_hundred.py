"""
Date: 06 01 2020
Author: Samantha Alcantara
Question: 
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
"""

#Answer

def near_hundred(n):
  if n >= 190 and n <= 210:
    return True
  if n>=90 and n<=110:
   return True
  else:
   return False
