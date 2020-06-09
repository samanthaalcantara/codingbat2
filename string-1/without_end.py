"""
Date: 06 08 2020
Author: Samantha Alcantara
Question: 
Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
"""

Answer:

def without_end(str):
  return str[1:-1]
