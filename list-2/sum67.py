"""
Date: 06 22 2020
Author: Samantha Alcantara
Question: 
Return the sum of the numbers in the array, 
except ignore sections of numbers starting with a 6 and 
extending to the next 7 (every 6 will be followed by at least one 7). 
Return 0 for no numbers.


def sum67(nums):
  for i in range(0, len(nums)):
    if nums[i] == 6:
      nums[i] = 0
      for j in range(i+1, len(nums)):
        temp = nums[j]
        nums[j] = 0
        if temp == 7:
          i = j + 1
          break
  return sum(nums)


#Answer

