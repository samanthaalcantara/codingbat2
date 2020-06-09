"""
Date: 06 08 2020
Author: Samantha Alcantara
Question: 
Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
"""

#Answer

def first_last6(nums):
  if 6 == nums[1:] or nums[:-1]:
    return True
  else:
    return False
    

