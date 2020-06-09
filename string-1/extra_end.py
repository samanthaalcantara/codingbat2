"""
Date: 06 08 2020
Author: Samantha Alcantara
Question: Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
"""

Answer:

def extra_end(str):
  return str[-2:] * 3 
