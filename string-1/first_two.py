"""
Date: 06 08 2020
Author: Samantha Alcantara
Question: 
Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
"""

Answer:
def first_two(str):
  if len(str) <= 2:
    return str
  return str[:2]
