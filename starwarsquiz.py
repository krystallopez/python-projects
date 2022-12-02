# A short interactive quiz that can be performed in the terminal
print("Hello! Welcome to the Stars Quiz! Let's see how much you know about Star Wars! May the Force be with you!\n")
print("Question 1: What year did the first Star Wars movie come out?\n")
answer_1 = input()

if answer_1 == "1977":
    print("That's right! Good job!\n")
else:
    print("Sorry, that's not the right answer. The correct answer is 1977.\n")


print("Alright, next question!")
print("What character is known for saying the phrase, 'Do or do not, there is no try'?\n")
answer_2 = input()

if (answer_2.lower() == "Yoda".lower()):
    print("With you strong the force is! Right the answer is.\n")
else:
    print("Fear is the path to the darkside. You are not correct.\n")

print("Let's keep it going!\n")
print("Question 3: What is baby Yoda's real name?\n")
answer_3 = input()

if (answer_3.lower() == "Grogu".lower()):
    print("You are on fire! You got it right!\n")
else:
    print("Ope. Sorry that is not the right answer.\n")

print("Let's get into some more questions!\n")
print("Question 4: Who is Palpatine's grandaughter?\n")
answer_4 = input()

if (answer_4.lower() == "Rey".lower()):
    print("You are correct, my apprentice..\n")
else:
    print("You have failed me for the last time. That is the wrong answer.\n")


print("Wow! You've made it so far! Let's keep going!\n")
print("Question 5: Who killed Qui-Gon Jinn?\n")
print("Hint: This one is kind of hard, but the killer looks the demon dude from Insidious\n")
answer_5 = input()

if (answer_5.lower() == "Darth Maul".lower() or "Maul".lower()):
    print("You are correct!\n")
else:
    print("Ooo. Better luck next time, that was the wrong answer!.\n")

print("Alright, next question!\n")
print("Question 6: Who was the Queen of Naboo and also served as a senator on the Galactic Senate?\n")
answer_6 = input("\n")

if (answer_6.lower() == "Padme Amidala".lower()):
    print("You got it right, great job!")
else:
    print("Sorry that answer is not correct. ")

print("Next question!\n")
print("Question 7: Which actor played Luke Skywalker?\n")
answer_7 = input("\n")

if (answer_7.lower() == "Mark Hamill".lower()):
    print("Woo! That is correct! ")
else:
    print("Sorry that answer is not correct. ")

print("We are almost at the end of the quiz, only 2 more questions left!\n")
print("Question 8:  What character did Carrie Fisher's daughter Billie Lourd play in Star Wars?\n")
answer_8 = input("\n")

if (answer_8.lower() == "Lieutenant Kaydel Connix".lower()):
    print("Yes! You got it! ")
else:
    print("Oof. Better luck next time kid, that was the wrong answer")

print("We are almost at the end of the quiz, only 2 more questions!\n")
print("Question 8:  What character did Carrie Fisher's daughter Billie Lourd play in Star Wars?\n")
answer_8 = input("\n")

if (answer_8.lower() == "Lieutenant Kaydel Connix".lower()):
    print("Yes! You got it! ")
else:
    print("Oof. Better luck next time kid, that was the wrong answer")


# need to find a way to keep score in the game
