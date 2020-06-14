"""
Date: 06 12 2020
Author: Samantha Alcantara
Question: The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.
"""


#Answer


def squirrel_play(temp, is_summer):
  if is_summer == True:
    return temp >= 60 and temp <=100
  return temp >= 60 and temp <=90

or

def squirrel_play(temp, is_summer):
  if is_summer == True:
   return 60 <= temp <= 100
  return 60 <= temp <= 90




-we need to decide if it is summer or not
-if is_summer == True we're going to return the temperature between 60 and up to 100
