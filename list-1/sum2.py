"""
Date: 06 08 2020
Author: Samantha Alcantara
Question: Given an array of ints, 
return the sum of the first 2 elements in the array. 
If the array length is less than 2, just sum up the elements 
that exist, returning 0 if the array is length 0.
"""

#Answer

def sum2(nums):
  if len(nums) == 0:
    return 0
  if len(nums) == 1:
    return nums[0]
  return nums[0] + nums[1]

