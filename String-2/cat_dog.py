"""
Date: 06 15 2020
Author: Samantha Alcantara
Question: 
Return True if the string "cat" and "dog"
appear the same number of times in the given string.
"""


#Answer

def cat_dog(str):
  count_cat = 0
  count_dog = 0
  for i in range(len(str)-2):
    if str[i:i+3] == 'dog':
      count_dog += 1
    if str[i:i+3] == 'cat':
      count_cat += 1
   
  return count_cat == count_dog
    

-catcount = 0 , counts the number of times that cat appears
-dogcount = 0, counts the number of times that dog appears
- we can generalize it to len(str)-3 but because we have to reach
1 we want to use < len(str) -2
