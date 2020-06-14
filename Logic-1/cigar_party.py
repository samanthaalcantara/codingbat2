"""
Date: 06 10 2020
Author: Samantha Alcantara
Question: When squirrels get together for a party, they like to have cigars. 
A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. 
Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
Return True if the party with the given values is successful, or False otherwise.
"""

#Answer

def cigar_party(cigars, is_weekend):
  if is_weekend:
   return True
  else:
   if cigars >= 40 and cigars <= 60 :
    return True
   else:
    return False
<<<<<<< HEAD
=======

  - simple if statement with a return inside 
  - if it is the weekend, were using a boolean statement
  - return cigars >= 40
  
  def cigar_party(cigars, is_weekend):
  if is_weekend == False:
   return cigars >= 40 and cigars <= 60
  return cigars >= 40
>>>>>>> 64cd4f5cee0f60192e1dfde3b756a59f385b28f4
