"""
Date: 06 15 2020
Author: Samantha Alcantara
Question: Given two strings, return True
if either of the strings appears at the
very end of the other string, ignoring upper/lower
case differences (in other words, the computation
should not be "case sensitive"). Note: s.lower()
returns the lowercase version of a string.
"""


#Answer

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return a[-(len(b)):] == b or a == b[-(len(a)):] 


-         01234              012345
- lstr = "Hiabc"     lstr = "abXabc"
          012                012
- sstr = "abc"       sstr = "abc"

