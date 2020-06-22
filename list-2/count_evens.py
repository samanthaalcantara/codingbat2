  
"""
Date: 06 22 2020
Author: Samantha Alcantara
Question: 
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
"""



#Answer


def count_evens(nums):
  count = 0
  for i in range(0, len(nums),1):
    if nums[i] % 2 == 0:
      count = count + 1
  return count 


-We're going to loop through the entire liste and check
each element in sequence to check if its even or odd.
-We will divide and even number by 2 to get 0 & an odd by
2 to get a remainder of 1
