<h1 align="center"> <b>Welcome To My Collection of Python Projects! </h1></b>

<p align="center" >
<img  width=400 src="Kylo-Ren-Approves.gif" alt="animated"/>
</p>

## Introduction 
This repo is a compilation of several different Python projects that I have built over the last couple of weeks. Feel free to browse through each of the files and check out some of my code! Enjoy and thank you for viewing!!

 
## Project 1: A Star Wars Interactive Quiz (CLI) 
This project is a fun  interactive quiz, that can be run within the terminal. The subject of the quiz is Star Wars! Every time the user gets a question right, they earn a point, however, if the user gets an answer wrong they don't earn any points. Using a score counter, the program is able to keep track of the user's score. Test your knowledge of Star Wars and see how many questions you can get right! May the force be with you!

## Project 2: Rock, Paper, Scissors Game (CLI)
The second project is a Rock, Papers scissors game, where you can choose Rock, Paper, or Scissors and see if you can beat the computer! This game was written in Python using lists and using the random module to generate a random item from the list when the user enters in their choice. May the odds be ever in your favor!

## Project 3: Password Generator 1 & 2

For my third project I created a random password generator. You enter in the length of the password and then the program will generate a password for you that consists of random letter, symbols, and numbers. For this project, I created two different versions of the password generator. In the file labeled passwordgen2.py, I used the random module and the string module so that I could define the data I was looking for, randomly sample different characters so that none of the characters are repeated, making for a very secure password. Once all of those characters are randomly generated, they are then joined  together in order to create the password. 

In the second file, passwordgen.py, I used three different lists compiled of letters, numbers, and symbols. There are two different ways that the problem could be solved. One way, we could just simply use a for loop and the range function, as well as the random module to randomly choose the specific letter, number, and symbol we want in the password. The password, a variable, being set as an empty string, we can then add each character to that variable. The second way that we can solve this problem is instead of storing the items from each list to an empty string, I stored each random character to a new list, and then shuffled through that list. After that, I then created a new password variable that is an empty string. I used a for loop to iterate through each separate character and added each character to the new password variable, them generating a new password for the user based on the number of letters, symbols, and numbers they have entered in the command line. 
