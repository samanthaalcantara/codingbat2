"""
Date: 06 22 2020
Author: Samantha Alcantara
Question: Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
"""


#Answer  
def sum13(nums):
 
  sum = 0
  if len(nums) > 0 and nums[0] ! = 13:
    sum = nums[0]
  for i in range(1,len(nums),1):
    if nums[i] ! = 13 and nums[i-1] ! = 13:
      sum = sum + nums[i]
  return sum





-We want to declare a sum and initalize it to 0
-See if the first element is 13
- We will need to loop to see if it was 13
-If the start of the loop is at index 0 then the program
will try to inspect the element at index -1  
