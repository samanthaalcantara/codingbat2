"""
Date: 06 12 2020
Author: Samantha Alcantara
Question: 
You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
"""



#Answer

def caught_speeding(speed, is_birthday):
  speed_adj = 0
  if (is_birthday == True):
    speed_adj = 5
  if speed < 61 + speed_adj:
    return 0
  if speed < 81 + speed_adj:
    return 1
  return 2


# no ticket      small ticket     big ticket

# 0 <= Speed < 61   61<= Speed < 81  Speed >= 81  
