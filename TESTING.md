# THE HANGMAN GAME
Developer: Maksim Popov

[Readme](README.md)
[Check Hangaman game on HEROKU]()


## Validator Testing
I used this site [ExtendsClass](https://extendsclass.com/python-tester.html) to check if I need to pay attention on something in my code. 
I got the next result ![ExtendsClass](https://i.ibb.co/ZKY41mM/Python-code.png)


| --TO BE TESTED--                                         | --ACTIONS--                            | --Expected outcome--                                                                 | --TEST RESULT--                 |   |   |
|----------------------------------------------------------|----------------------------------------|--------------------------------------------------------------------------------------|---------------------------------|---|---|
| Introduction                                             | Run the terminal. Scroll up and down.  | Displays game rules                                                                  | Test passed. Works as expected. |   |   |
| Prompt: Fancy to hear  a rhyme?                          | Run terminal, requires to press Y or N | Only accepted "Y" / "N". Others values not accepted and it requires to repeat entry. | Test passed. Works as expected  |   |   |
| Prompt: Fancy to hear  a rhyme?                          | Press "N" or "n"                       | Skips the rhyme and asks if player wants to play a game                              | Test passed. Works as expected  |   |   |
| Prompt: Fancy to hear  a rhyme?                          | Press "Y" or "y"                       | Shows the rhyme, and asks if player wants to play a game                             | Test passed. Works as expected  |   |   |
| Prompt: Fancy to hear  a rhyme?                          | Press "1", "a", "yy", "ny", "#"        | Requests to enter "Y" or "N"                                                         | Test passed. Works as expected  |   |   |
| Prompt: Are you ready to start the game? Press ('Y'/'N') | Press "N" or "n"                       | Exit the Game                                                                        | Test passed. Works as expected  |   |   |
| Prompt: Are you ready to start the game? Press ('Y'/'N') | Press "Y" or "y"                       | Request Player to enter name                                                         | Test passed. Works as expected  |   |   |
| Prompt: Are you ready to start the game? Press ('Y'/'N') | Press "5", "f", "yy", "ny", "#"        | Requests to enter "Y" or "N"                                                         | Test passed. Works as expected  |   |   |
| Prompt: Please enter your name:                          | Enter "a", "5", "65", "re5", "##"      | Don't accept these values and asks to enter name again                               | Test passed. Works as expected  |   |   |
| Prompt: Please enter your name:                          | Input letters, 2 and more              | Sets first letter capital and moves to question about selecting game difficulty      | Test passed. Works as expected  |   |   |
| Prompt: Choose your number (difficulty level)            | Accepts only 4 numbers: 1, 2, 3, 4     | Accepts value, and displays hidden word.                                             | Test passed. Works as expected  |   |   |
| Prompt: Choose your number (difficulty level)            |  Input: Any other value                | Don't accept it, and requests to put value between 1 and 4                           | Test passed. Works as expected  |   |   |
| Prompt: Please enter a  letter                           | Input correct letter                   | Displays letter, asks for another letter                                             | Test passed. Works as expected  |   |   |
| Prompt: Please enter a  letter                           | Input incorrect letter                 | Shows it is incorrect, checks attempts > 0, shows hangman picture, asks for a letter | Test passed. Works as expected  |   |   |
| Prompt: Please enter a  letter                           | Input incorrect letter (0 attempts)    | Outcome: completed picture of hangman, no attempts left, you lose ask to start again | Test passed. Works as expected  |   |   |
| Prompt: Would you like to start again?                   | "N" or "n"                             | Exit game                                                                            | Test passed. Works as expected  |   |   |
| Prompt: Would you like to start again?                   | "Y" or "y"                             | Asks to pick up difficulty                                                           | Test passed. Works as expected  |   |   |
| Prompt: Would you like to start again?                   | Only accepts Y or N, no other values   | Requests to enter "Y" or "N"                                                         | Test passed. Works as expected  |   |   |
|                                                          |                                        |                                                                                      |                                 |   |   |

					