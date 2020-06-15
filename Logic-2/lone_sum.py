"""
Date:06 13 2020
Author: Samantha Alcantara
Question: 
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.
"""


#Answer

def lone_sum(a, b, c):
  if a == b == c:
   return 0
  if  b == c:
   return a
  if a == c:
   return b
  if a == b:
   return c
  return a + b + c
  
  
   
