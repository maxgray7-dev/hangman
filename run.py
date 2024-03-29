# import modules


import random  # generates random words for the game
import string  # format letters to uppercase
import sys  # this allows to close the game if player don't want to play

#  7 drawings imported from module and represent lives in the game

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

#  code for game


def introduction():
    """
    This section explains game rules to the player.
    """
    print("_"*70)
    print(" " * 8 + "*" * 30)
    print("**********WELCOME TO THE HANGMAN GAME *********")
    print(" " * 8 + "*" * 30)
    print(" " * 8 + "*" * 30)
    print("                     RULES\n")
    print("1. Attention!! In this game you can select level of difficulty.")
    print("2. There is a random word will be chosen by computer.")
    print("3. Computer will display shows number of hidden letters.")
    print("4. Guess a letter, and if it in the word computer displays it. ")
    print("                         BUT")
    print("5. Be careful, you have 7 attempts to succeed.")
    print("6. When hangman drawing is fully completed - computer wins.")
    print("                     Good Luck!")
    print("_"*70)


def rhyme():
    """This function will ask player if he is ready to play"""
    while True:
        response = input("Fancy a hangman rhyme?('Y'/'N')\n").strip().upper()
        if response == 'Y':
            print(("_" * 80))
            print("*****      THE HANGMAN GAME RHYME                 *****")

            print("*****  In Hangman's play, a word concealed,       *****")
            print("*****  Guessing letters, fate's revealed.         *****")
            print("*****  Each wrong guess brings the gallows near,  *****")
            print("*****  But solve the puzzle, redemption's cheer.  *****")
            print((" " * 8 + "*" * 30))
            print((" " * 8 + "*" * 30))
            break
        elif response == 'N':
            print("")
            break
        else:
            print("Sorry, I didn't get this, please enter 'Y' or 'N'")
    return response


def library_choice():
    """
    Player picks the category for playing games
    """
    library = {1: "book_1", 2: "book_2", 3: "book_3", 4: "book_4"}
    #  Difficulty level
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

            #  IF statement picks random word from chosen library
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


def hangman_picture(attempt):
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
    """Function to ask player his name"""
    while True:
        name = input("Please enter your name: ")
        if name.isalpha() and len(name) > 1:
            return name.title()
        else:
            print("Invalid value. Please enter your name again: ")


def ready_to_play():
    """This function will ask player if he is ready to play"""
    while True:
        response = input("Are you ready to start?('Y'/'N')\n").strip().upper()
        if response == 'Y':
            print("Be brave human! We start now!")
            break
        elif response == 'N':
            print("Good bye human! Maybe another time")
            sys.exit()
        else:
            print("Sorry, I didn't get this, please enter 'Y' or 'N'")
    return response


def hidden_word():
    'Displays hidden word and responds for the decreasing attempts'
    #  variables that I will use in this function
    the_word = random_word().upper()
    alphabet = set(string.ascii_uppercase)
    the_word_letters = set(the_word.upper())  #  letters from the_word
    named_letters = set()  # letters player used already
    my_list = ["_"] * len(the_word)
    attempt = 7  # Player has 7 attempts

    while "_" in my_list and attempt > 0:
        print(" " * 40, " ".join(my_list))
        new_letter = input("Please enter a letter!\n").upper().strip()

        if new_letter in alphabet - named_letters:
            named_letters.add(new_letter)  # add new letter to the list

            if new_letter in the_word_letters:
                the_word_letters.remove(new_letter)
                print(f"Good Job!! You guessed correct'{new_letter}'")

            elif new_letter not in the_word_letters:
                print(f"Alas! This is incorrect! No letter: '{new_letter}'")
                attempt -=1
                hangman_picture(attempt)  # this displays the hangman picture

                if attempt == 0:  # This checks if player has attempts
                    print(f"Sorry! No '{new_letter}'in this word! You lost")
                    print("The word you tried to guess was: ", the_word)
                    print(("_") * 70)
                    print((("_") * 25) + ("") * 20 + ("_") * 25)
                    print("\nYOU LOSE!")
                    print((("_") * 25) + ("") * 20 + ("_") * 25)
                    print(("_") * 70)
                    named_letters.clear()

                    while True:
                        restart = input("Start again? Y/N\n").strip().upper()

                        if restart == 'Y':
                            return True
                        elif restart == 'N':
                            return False
                        else:
                            print("Sorry, I didn't get it, please enter Y/N")

            for i, letter in enumerate(the_word):
                if letter == new_letter:
                    my_list[i] = new_letter

        elif new_letter in named_letters:
            print("You tried this letter before. Please enter another letter!")
        else:
            ("Invalid value, please enter another letter!")
        print("You have left attempts:", attempt)
        print("You used next letters:", ", " .join(named_letters))
    print("\n You won! The word is:", " ".join(my_list))
    print(" ")
    print(" " * 18 + "*" * 30)
    while True:
        restart = input("Start again? Y/N\n").strip().upper()

        if restart == 'Y':
            return True
        elif restart == 'N':
            return False
        else:
            print("Sorry, I didn't get this, please enter 'Y' or 'N'")


def main():
    introduction()
    rhyme()
    ready_to_play()
    greetings_player(get_name)()

    while True:
        restart = hidden_word()
        if not restart:
            break


main()