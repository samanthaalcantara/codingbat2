"""
Date: 06 01 2020
Author: Samantha Alcantara
Question:
Given an int n, return the absolute difference between n and 21, except return  double the absolute difference if n is over 21.
""" 

#Answer
def diff21(n):
  if n <= 21:
    return 21 - n
  else:
      return(n-21)*2
