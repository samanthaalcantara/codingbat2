"""
Date: 06 15 2020
Author: Samantha Alcantara
Question; Return True if the given string
contains an appearance of "xyz" where the xyz 
is not directly preceeded by a period (.). So
"xxyz" counts but "x.xyz" does not.
"""


#Answer

def xyz_there(str):def xyz_there(str):
  for i in range(len(str)):
    if str[i] != '.' and str[i+1:i+4] == 'xyz':
      return True
  if str[0:3] == 'xyz':
    return True
  return False



-Fun one-liner that is a nice practice in stringing 
together function 

- str = abc.xyzxyz
- str.replace(".xyz", "")   abcxyz

