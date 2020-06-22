"""
Date: 06 15 2020
Author: Samantha Alcantara
Game:Dice Roller



Instructions:

Anytime were creating a game to generate random numbers,
were going to use the random module, "import random".
We'll use a function called  def dice_roll():
so it will return the value that is randomly generated
& then we will setup a variable diceroll = random.randint (1, 6)
1 being the first number and 6 being the last number to be generated 
and any number in between 1-6. 
We're going to setup a main function called def main() and add players 1
& player 2 to see if the dice generates less than, greater than or equal to.
I have it setup for the players to have 9 rounds using the while loop and then
printing an added string. We use the number 10 to have 9 rounds.
The generator pulls a random number from the function player1 = dice_roll() and
gives it to player 1. & then we add player 2 and the generator pulls a random number 
from the function player2 = dice_roll(). We can add more information using the string
method to generate words that say Player 1 Roll. Using the else/if statement we can
add if player 1 == player 2: print("Draw") . Or elif player1 > player2: print("player 1 wins")
else print("player 2 wins"). "Rounds = rounds + 1" whoever wins gets a point added to their score.















import random


def main(): 
    player1 = 0
    player1wins =0
    player2 = 0
    player2wins = 0
    rounds = 1

    while rounds != 10:
        print("Round " + str(rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        print("Player 1 Roll: " + str(player1))
        print("Player 2 Roll: " + str(player2))

        if player1 == player2:
            print("Stalemate!")
        elif player1 > player2:
            player1wins = player1wins + 1
            print("Alejandro Rolls He Scores!")
        else:
            player1wins = player1wins + 1
            print("Nataya Rolls She Scores!")

        rounds = rounds + 1

    if player1wins == player2wins:
        print("Draw!")
    elif player1wins > player2wins:
        print("Player 1 Scores, Congratulations Alejandro:You are the Winner! - Round Won : " + str(player1wins))
    else:
        print("Player 2 Scores, Congratulations Nataya:You are the Winner! - Round Won : " + str(player2wins))

def dice_roll():
    diceroll = random.randint(1,6)
    return diceroll








