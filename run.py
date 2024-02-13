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

from book_1 import WORDS_1    # words that game will randomly use
from book_2 import WORDS_2
from book_3 import WORDS_3
from book_4 import WORDS_4

# code for game


def introduction():
    """
    This section explains game rules to the player.
    """
    print("_"*70)
    print("\nWELCOME TO THE HANGMAN GAME\n ")
    print("_"*70)
    print("The objective of the game is simple:\n")
    print("Computer picks a hidden word.")
    print("The player has to guess and pick a letter.")
    print("If the word has picked letter, it opens in the hidden word.")
    print("Player continues guessing until:")
    print("player opens entire word or guesses incorrectly.")
    print("If letter absent - computer displays a part of hangman drawing.")
    print("When hangman drawing completed - computer wins")
    print("Player wins if hidden word opened before hangman pic completed.\n")
    print("_"*70)
    print("\nPlayer has 7 attempts before 'Hangman' completed")
    print("_"*70)


def word_choice():
    """
    Computer picks the random word from the library
    """
    
