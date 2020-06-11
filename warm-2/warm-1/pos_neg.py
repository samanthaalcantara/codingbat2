"""
Date: 06 01 2020
Author: Samantha Alcantara
Question: 
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
"""

#Answer

def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
    
  # if (a > 0 and b > 0) or (a < 0 and b > 0): 
  # return True
  # if (a < 0 and b < 0):
  #   return True
  # else:
  #   return False
  

#1)a > 0 and b < 0  or a < 0 and b > 0 -> true
#2) when negative is true, a < 0 and b < 0 -> return true
#3) anything else return false

def pos_neg(a,b,negative):
  if negative:
    return(a<0 and b<0)
  else:
      return((a<0 and b>0) or (a>0 and b<0))
