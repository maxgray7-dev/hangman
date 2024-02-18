# THE HANGMAN GAME
developer: Maksim Popov


The hangman game is a popular game about guessing a word that computer selected. The player will have 7 lives, that represented as a hangman picture. 

The game with computer, that will pick a random word. After picking the word, computer asks a player to name a letter. If letter was picked correctly, computer opens the letter and continues asking the player again to provide a letter, until the whole word is opened. However, if player provides incorrect letter, then  computer starts drowing the hangman picture. 
After each incorrect answer computer adds additional human parts to the  drawing.  If player will guess the word before the picture completed, player wins. Meanwhile if computer finish the picture - computer wins.


# Content

- [User Experience (UX)](#user-experience)
- [Planning ](#planning)
- [Features ](#features)
- [Tecnologies used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## User Experience


### Project goal
The game objective to have a quick game that can take not longer then 2-3 mins
It helps players to learn new english words
It suits great for quick breaks to relaxcwith simple game controls.
The game is easy to understand and with intuitive game play.

### Who can be user
User can be anyone who just need to do a short break.
Good for an office worker or student, but it can be good for anyone.

### As a developer, I would expect:
 - easy game dynamic
 - fast gameplay
 - a good fun for user
 - users can increase vocabulary by playing


## Planning

### Lucid Chart
To imagine process and functions I need I used Lucid Chart. I made a chart that helped me imagine better the way of coding my project.
This helped me to understand directions during my coding process and what exactly I need.
![Lucid Chart sketch](https://i.ibb.co/LnnLCGk/Lucidchart-hangman.png)


## Features and Functionalities

### Playing game
The goal of this game is for player to guess a word that computer picked.
I created for player 4 libraries, which can pick from easy to hard words.

### Features
 In introduction game introduces player with the rules of the game and asks if he is ready ti play.
 If Player agrees with the statement, he must press "Y" or "N". Option N, closing the terminal where is Y takes player to the next step where computer asks to enter  the name.
 Name can be accepted only if used letters and more than 1 letter, also the first letter will be capitalised. 
 





## Credits
In my work I used libraries and videos to learn techniques and commands to complete my project.
I found several advices about what can be used for building this game, and I will share those sources in this section:
[W3Schools](https://www.w3schools.com/python/ref_func_str.asp) help to learn methods and functions
[Pythonpool]( https://www.pythonpool.com/check-data-type-python/) - is additional site to help with understanding how to find type of file.
[Chat_GPT] It helped me with  finding errors in my code if I spent too much time and required help of mentor.
[Youtube - Hangman Project](https://www.youtube.com/watch?v=m4nEnsavl6w&t=294s) I found several useful videos, where people showed how they built this game.
        It was very helpful to see what exactly options they used and many carious approaches.
[Youtube - Decorators](https://www.youtube.com/watch?v=MYAEv3JoenI) I had a lot of time as couldn't wrap my head around decorations this video helped a lot.

 