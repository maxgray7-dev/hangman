# THE HANGMAN GAME
Developer: Maksim Popov


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
 
To make game more fun, I used chat GPT to create a short and funny poem about hangman game which should encorane player.
After this computer confirm if pplayer ready to play, and if yes than it displays hidden word to the player that he should guess.
After finishing the game computer asks player if he would like to continue and if yes, player must pick again level of difficulty and to guess a new word.
![Picture_from_the_game](https://i.ibb.co/kK11Q5K/Hangman.png)

As a futures of the game I would 


## Technologies used

[Python](https://www.python.org) - Programming Language that was used in this project.
[ExtendsClass](https://extendsclass.com/python-tester.html) check for errors
[GitHub](https://github.com/) store project in cloud
[Codeanywhere](https://app.codeanywhere.com/workspace) IDE which sometimes worked and usually not, but was used in the beginning of the project.
[VSCode](https://code.visualstudio.com/) - Local Integrated Development Environment(IDE) which I tried to use in this project.
[GitPod](https://www.gitpod.io/) Primary Integrated Development Environment(IDE) that I used for this project 
[Lucidchart](https://www.lucidchart.com/pages/) used to create a sketch of project.
[ImgBB](https://imgbb.com) - icloud storage, used for saving screenshoots and uploading to my readme file.
[Am I Responsive?](http://ami.responsivedesign.is) used to show how project looks on screens
[Table Convert](https://tableconvert.com/) - used to create a table for Testing MD file
[Chat GPT](https://chat.openai.com/) Tool that I mainly use for debugging and answering my questions.
[Youtube](https://www.youtube.com/) watching learning videos and examples to understand how problem can be solved.
[Heroku](https://dashboard.heroku.com/apps) Cloud platform used for deployment this project.

### Future additions and improvements
- I would consider to add more libraries with different themes and more words
- It would be good to add scores player VS computer
- Include an option to enter the whole word
- Use more design techniques to make gave visually more interesting

### Modules imported
In current project were imported several modules:

- random module  - generates random choices (numbers, sequences, choices, words)
- string module - quickly access some string constants, and manipulate string data, at example checking character sets.
- sys module - allow player to exit game when he choces answer 'N' on the question do you want to play game?


## Deployment 

### Heroku

I used Heroku to deploy this project on icloud. To process, required next steps:
Go to [HEROKU](https://dashboard.heroku.com/apps)
1 - Log in to Heroku
2 - Click "New"
3 - Create a new app
4 - Choose the app name and region
5 - Navigate to the "settings" tab.
6 - Click "Reveal Config Vars".
7 - Add a configuration variable to Heroku's Settings. The key is PORT and the value is 8000
8 - Scroll down to "Buildpacks".
9 - Click "Add Buildpack".
10 -First, add "python" and click save.
11 -Second, add "nodejs" and click save.

The live site can be found here: [Hangman Game]()

### Cloning
 Go to [GitHub](https://github.com/) and follow next steps:
 1 - Click button "Code" that can ve found in GitHub Repository
 2 - Select "HTTPS" and copy the link.
 3 - Use GitBush in window and open terminal and navigate to the repository where you need to paste cloned reposotory(repo)
 4 - Enter "git clone" followed by the copied link
 5 - Press "Enter" to clone repo.

 ### Forking 
 Forking allows to copy the project and copy to your own GitHub. Which will allow to work and change it.
 To do forking requie to complete next step. Go to [GitHub](https://github.com/)
 1 - Select required repo
 2 - On the top right screen, can be found a button with "Fork" label. Click it.


## Credits

To comlete this project, I complited my lessons on codeinstitute including exercices that helped me with practicing and developing visual understanding.
In my current work I used libraries and videos to learn techniques and commands to complete my project.
I found several advices for building this game, and I will share those sources in this section:

[Code Institute](https://learn.codeinstitute.net/ci_program/diplomainfullstacksoftwarecommoncurriculum)
[W3Schools](https://www.w3schools.com/python/ref_func_str.asp) help to learn methods and functions
[Pythonpool]( https://www.pythonpool.com/check-data-type-python/) - is additional site to help with understanding how to find type of file.
[Chat_GPT] It helped me with  finding errors in my code if I spent too much time and required help of mentor.
[Youtube - Hangman Project](https://www.youtube.com/watch?v=m4nEnsavl6w&t=294s) I found several useful videos, where people showed how they built this game. Helpful to see options they used and other techniques.
[Youtube - Decorators](https://www.youtube.com/watch?v=MYAEv3JoenI) I had a lot of time as couldn't wrap my head around decorations this video helped a lot.

## Acnowledgement
I am very grateful for the help of my mentor Chris Quinn who constantly help me to overcome the stress, and capable to motivate me for my next achievement and future development.
I also would like to say thank you to Stefania Frustagli, who is my friend. She often helps me with advices and suggestions how to succeed in my projects.
