"""
Date: 06 08 2020
Author: Samantha Alcantara
Question: Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
"""

Answer:

def non_start(a, b):
  return a[1:] + b[1:]

