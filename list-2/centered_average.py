"""
Date: 06 22 2020
Author: Samantha Alcantara
Question: 
Return the "centered" average of an array of ints, 
which we'll say is the mean average of the values, 
except ignoring the largest and smallest values in the array. 
If there are multiple copies of the smallest value, ignore just one copy, 
and likewise for the largest value. Use int division to produce the final average. 
You may assume that the array is length 3 or more.
"""


#Answer


def centered_average(nums):
  sum = 0 
  maxv = max(nums)
  minv = min(nums)
  for i in range(0,len(nums),1):
    sum = sum + nums[i]
  return (sum - maxv - minv)/(len(nums) - 2)









-We're going to find the sum of the list and subtract
the largest and smallest elements.
-Divide that by the length of the list minus 2
-Find the sum of the list
-Find the Maximum and Minimum Value in the list
