"""
Date: 06 01 2020
Author: Samantha Alcantara
Question:  
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
"""

#Answer

def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str
  
def not_string(str):
  a + str.split('not')
  if len(a) > 1 and a [0] =="":
    return str
  else:
      return 'not ' + str
