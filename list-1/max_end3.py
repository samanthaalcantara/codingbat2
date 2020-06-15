"""
Date: 06 08 2020
Author: Samantha Alcantara
Question: Given an array of ints length 3, 
figure out which is larger, the first or last 
element in the array, and set all the other elements 
to be that value. Return the changed array.
"""

#Answer

def max_end3(nums):
  m = max(nums[0], nums[2])
  return [m, m, m]


