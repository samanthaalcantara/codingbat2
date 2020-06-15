"""
Date: 06 08 2020
Author: Samantha Alcantara
Question: 
Given an array of ints, return a new array length 2 
containing the first and last elements from the original array. 
The original array will be length 1 or more.
"""

#Answer

def make_ends(nums):
  return [nums[0], nums[-1]]

