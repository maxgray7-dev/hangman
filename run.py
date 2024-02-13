# import modules


import random  # generates random words for the game
import string  # format letters to uppercase

# 7 drawings imported from module and represent lives in the game

from hangman import (
    hangman_1,
    hangman_2,
    hangman_3,
    hangman_4,
    hangman_5,
    hangman_6,
    hangman_7
)

from dictionary import WORDS    # words that game will randomly use

# code for game


def introduction():
    """
    This section explains game rules to the player.
    """
    print("WELCOME TO THE HANGMAN GAME\n ")
    print("The objective of this game is simple:\n")
    print("Computer picks a hidden word.")
    print("The player has to guess, by suggesting letters one by one.")
    print("If letter picked right, it opens in the hidden word.")
    print("Player continues to call letter by letter until:")
    print("opens full word or guess incorrectly.")
    print("When letter picked wrong the computer displays a part of hangman.")
    print("When drawing completed the game comes to the end - player loses")
    print("Player wins if opens the hidden word before computer finishes")
    


