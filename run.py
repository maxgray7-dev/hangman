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
    print("The objective of this game is simple:\n")
    print("There is a random word")
    print("Computer displays how many letters in it")
    print("Name a letter, and if the word has it, ")
    print("that letter/s will be placed in the word")
    print("You will have 7 attempts to open the word")
    print("When hangman drawing fully completed - computer wins")
    print("_"*70)


def library_choice():
    """
    Player picks the category for playing games
    """
    library = {1: "book_1", 2: "book_2", 3: "book_3", 4: "book_4"}   
    # Difficulty level
    print("Select difficulty level:")
    print("1 - Easy")
    print("2 - Normal")
    print("3 - Advanced (phrases)")
    print("4 - Hard")

    while True:
        print("please pick the number from 1 - 4")
        player_choice = input("Choose your number wisely:\n").strip()

        if player_choice in ["1", "2", "3", "4"]:
            difficulty_level = int(player_choice)
            library_selection = None

            if difficulty_level == 1:
                library_selection = WORDS_1
                print("\n You selected difficulty Level: EASY")
                break              

            elif difficulty_level == 2:
                library_selection = WORDS_2
                print("\n You selected difficulty Level: Normal")
                break

            elif difficulty_level == 3:
                library_selection = WORDS_3
                print("\n You selected difficulty Level: Advanced")
                break

            elif difficulty_level == 4:
                library_selection = WORDS_4
                print("\n You selected difficulty Level: Hard")
                break

            # IF statement picks random word from chosen library
            if library_selection:
                random_word = random.choice(library_selection)
                return random_word.upper()

            else: 
                print("Incorrectly selected difficulty level")
                print("Please select the difficulty level 1, 2, 3 or 4")
    return library_selection



    """
    Replaces random word with dashes
    """
def hidden_word():
    """This function replaces the picked by computer word with underscores"""
    random_word = library_choice()
    num_of_letters = len(random_word) * " _"
    return num_of_letters


def game_process():
    



def main():
    introduction()
    library_choice()
    print(hidden_word())