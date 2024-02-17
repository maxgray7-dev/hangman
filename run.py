# import modules


import random  # generates random words for the game
import string  # format letters to uppercase
import sys # this allows to close the game if player don't want to play

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
    print(" "*8 +"*" * 30)
    print("**********WELCOME TO THE HANGMAN GAME *********")
    print(" "*8 +"*" * 30)
    print(" "*8 +"*" * 30)
    print("The Hangman GOAL is quite simple:\n")
    print("There is a random word picked, you chose difficulty.")
    print("Computer will display then number of letters in it")
    print("Guess a letter, and if the word has it, ")
    print("that letter or letters appear in the word")
    print("Be careful, You have 7 attempts to open the word")
    print("When hangman drawing fully completed - computer wins")
    print("Good Luck!")
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
    print("3 - Advanced")
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


def random_word():
    """This function displays the word computer picked"""
    word = random.choice(library_choice())
    return word



def hangman_picture (attempt):
    """Displays a hangman picture which depends on attempts left"""
    if attempt == 6:
        hangman_1()
    elif attempt == 5:
        hangman_2()
    elif attempt == 4:
        hangman_3()
    elif attempt == 3:
        hangman_4()
    elif attempt == 2:
        hangman_5()
    elif attempt == 1:
        hangman_6()
    else:
        hangman_7()  


def greetings_player(func):
    """Decorator function to welcome a player """
    def inner():
        name = func()
        print(f"\nHi {name}! Welcome to the game, Let's have fun!")
        print("="*70)

    return inner

def get_name():
    while True:
        name = input("Please enter your name: ")
        if name.isalpha() and len(name) > 1:
            return name
        else:
            print("Invalid value. Please enter your name again: ")
        


def ready_to_play():
    """This function will ask player if he is ready to play"""
    while True:
        response = input("Are you ready to start? Press ('Y'/'N')\n").strip().upper()
        if response == 'Y':
            print("Be brave human! we start now!")
            break
        elif response == 'N':
            print("Good bye human! Maybe another time")
            sys.exit()
        else:
            print("Sorry, I didn't get this, please enter 'Y' or 'N'")
    return response


def hidden_word():
    'This function displays hidden word and responds for the decreasing attempts'
    # variables that I will use in this function
    the_word = random_word().upper()
    alphabet = set(string.ascii_uppercase)
    the_word_letters = set(the_word.upper()) # letters from the_word
    named_letters = set() # letters player used already
    my_list = ["_"] * len(the_word) # the_word
    attempt = 7 # Player has 7 attempts


    while "_" in my_list and attempt > 0 :
        print(" ".join(my_list))
        new_letter = input("Please enter a letter!\n").upper().strip()

        if new_letter in alphabet - named_letters:
            print("HERE ", new_letter, type(new_letter))
            named_letters.add(new_letter) # add new letter to the list

            if new_letter in the_word_letters:
                the_word_letters.remove(new_letter)
                print(f"Good Job!! You guessed correct! This word has the letter: '{new_letter}'")

            elif new_letter not in the_word_letters:
                print(f"Alas! This is incorrect! This word has no letter: '{new_letter}'")
                attempt -=1
                hangman_picture(attempt) # this should display the hangman picture
                    
                if attempt == 0: # This checks after each answer if player has attempts
                    print(f" Sorry. No '{new_letter}' in this word ! You have no more attempts! You lost")
                    print("The word you tried to guess was: ", the_word)
                    print(("_") * 70)
                    print((("_") * 25) + ("") * 20 + ("_") * 25)
                    print("\nYOU LOSE!")
                    print((("_") * 25) + ("") * 20 + ("_") * 25)
                    print(("_") * 70)
                    named_letters.clear()

                    while True:
                        restart = input("Would you like to restart and have another chance? Y / N\n").strip().upper()

                        if restart == 'Y':
                            return True
                        elif restart == 'N':
                            return False
                        else:
                            print("Sorry, I didn't get this, please enter 'Y' or 'N'")
            
            for i, letter in enumerate(the_word):
                #print("loop ", letter, new_letter)
                if letter == new_letter:
                    my_list[i] = new_letter
                    
        elif new_letter in named_letters:
                print("You tried this letter before. Please enter another letter!")
        else:
                ("Invalid value, please enter another letter!")
        print("You have left attempts:", attempt)
        print("You used next letters:", ", " .join(named_letters))
    print("\n You won! The word is:", " ".join(my_list))
    while True:
        restart = input("Would you like to restart and have another chance? Y / N\n").strip().upper()

        if restart == 'Y':
            return True
        elif restart == 'N':
            return False
        else:
            print("Sorry, I didn't get this, please enter 'Y' or 'N'")



def main():
    introduction()
    ready_to_play()
    greetings_player(get_name)()

    while True:
        restart = hidden_word()
        if not restart:
            break



main()  