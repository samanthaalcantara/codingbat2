"""
Date: 06 22 2020
Author: Samantha Alcantara
Question: Return the sum of the numbers in the array, r
eturning 0 for an empty array. Except the number 13 is very unlucky, 
so it does not count and numbers that come immediately after a 13 also do not count.
"""


#Answer  
def sum13(nums):
  if len(nums) == 0:
    return 0
 
  for i in range(0, len(nums)):
    if nums[i] == 13:
      nums[i] = 0
      if i+1 < len(nums): 
        nums[i+1] = 0
  return sum(nums)





-We want to declare a sum and initalize it to 0
-See if the first element is 13
- We will need to loop to see if it was 13
-If the start of the loop is at index 0 then the program
will try to inspect the element at index -1  """
Date: 06 22 2020
Author: Samantha Alcantara
Question: 
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


#Answer

