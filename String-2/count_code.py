"""
Date: 06 15 2020
Author: Samantha Alcantara
Question: Return the number of times that the
string "code" appears anywhere in the given string,
except we'll accept any letter for the 'd', so "cope"
and "cooe" count.
"""

#Answer 

def count_code(str):
  count = 0
  for i in range(0, len(str)-3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      count += 1
  return count




-str = 0123456789    str[0:4]
       aaacodebbb    str[6:10]
-w = 0123   w[0:2]
     code   w[3]




