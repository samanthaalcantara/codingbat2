"""
Date: 06 17 2020
Author: Samantha Alcantara
Question: Given a string, return a string where 
for every char 
in the original, there are two chars.
"""


#Answer

def double_char(str):  
  result = ""
  for i in range(0,len(str),1): 
    result = result + str[i] + str[i]
  return result

-We are building a string and then altering it so that or every character
there are two of the same characters

- T + T + h + h + e + e
