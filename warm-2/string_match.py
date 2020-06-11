"""
Date: 06 07 2020
Author: Samantha Alcantara
Question: Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
"""

#Answer

def string_match:
  def string_match(a, b):
  min_length = min(len(a),len(b))
  count = 0
  for i in range (min_length-1):
    if a [i:i:+2] == b[i:i+2]:
      count += 1
      return count
