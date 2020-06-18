"""
Date: 06 15 2020
Author: Samantha Alcantara
Game:Dice Roller



Instructions:













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








