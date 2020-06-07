""""
Date: 06 07 2020
Author: Samantha Alcantara
Question: 
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
  result = ''
  for n in range(0, len(str)):
    if n%2 == 0:
      result += str[n]
  return result
