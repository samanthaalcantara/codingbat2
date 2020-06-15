"""
Date: 06 15 2020
Author: Samantha Alcantara
Title: Dice Roller



def dice_roll():
    diceroll = random.randit(1,6)
    return diceroll

def main():
    player1 = 0
    player1wins = 0
    player2 = 0
    player2wins = 0
    rounds = 2

while rounds != 12
   print("Round " + str(rounds))
   player1 = dice_roll()
   player2 = dice_roll()
   print("Player 1 Roll: " + str(player1))
   print("Player 2 Roll: " + str(player2))

   if player1 == player2:
       print("Draw!!/n")
   elif player1 > player2:
       player1wins = player1wins + 1
       print("Player 1 Wins!!/n")
   else:
      player2wins = player2wins + 1
      print("Player 2 Wins!!/n")

   rounds = rounds + 1

   if player1wins == player2wins:
       print("Draw!!")  
   elif player1wins > player2wins:
      print("Player 1 Wins! - Rounds Won: " + str(player1wins))
   else:
      print("Player 2 Wins! - Rounds Won: " + str(player2wins))


