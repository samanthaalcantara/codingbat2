"""
Date: 06 08 2020
Author: Samantha Alcantara
Question: Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
"""

#Answer

def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]] 
