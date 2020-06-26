"""
Date: 06 13 2020
Author: Samantha Alcantara
Question: 
We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops.
"""

#Answer

def make_bricks(small, big, goal):
  if small >= goal:
    return True
  elif big * 5 + small < goal:
    return False
  elif big != 0 and goal % (big * 5) <= small:
    return True
  elif big * 5 > goal and (goal % 5 == 0 or goal % 5 <= small):
    return True
  else:
    return False 
