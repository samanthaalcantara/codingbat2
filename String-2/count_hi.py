"""
Date: 06 17 2020
Author: Samantha Alcantara
Question: 
Return the number of times that the string "hi"
 appears anywhere in the given string.
"""


#Answer

def count_hi(str):
  count = 0
  for i in range(0,len(str)-1,1):
    if str[i:i+2] == "hi":
        count = count + 1
  return count


- str = abc hi ho 
-The length is 9 
-Index is 0-8
-frame size 2

- str[0:2] =  "ab"
-str[7:9] = "ho"
-count = 0
