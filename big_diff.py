"""
Date: 06 22 2020
Author: Samantha Alcantara
Question: 
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
"""


#Answer

def big_diff(nums):
  maxv = nums[0]
  minv = nums[0]
  
  for i in range(0,len(nums),1):
    if maxv < nums[i]:
      maxv = nums[i]
    if minv > nums[i]:
      minv = nums[i]
  return maxv - minv

-Initialize the max value to an element of 0 to find 
the max value
