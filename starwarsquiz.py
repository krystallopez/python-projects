# A short interactive quiz that can be performed in the terminal
print("Hello! Welcome to the Stars Quiz! Let's see how much you know about Star Wars! May the Force be with you!\n")
print("Question 1: What year did the first Star Wars movie come out?\n")
answer_1 = input()
score = 0

if answer_1 == "1977":
    score += 1
    print(f"\nThat's right! Good job! You earned {score} point(s). \n")
    print(f"Your score is now: {score}\n")
else:
    score -= 1
    print(f"\nSorry, that's not the right answer. The correct answer is 1977. You score is {score} point(s). \n")
    print(f"Your score is now: {score}.\n")


print("Alright, next question!\n")
print("What character is known for saying the phrase, 'Do or do not, there is no try'?\n")
answer_2 = input()

if (answer_2.lower() == "Yoda".lower()):
    score += 1
    print(f"\nWith you strong the force is! Right the answer is. You earned {score} point(s).\n")
    print(f"Your score is now: {score}\n")
else:
    score -= 1
    print(f"\nFear is the path to the darkside. You are not correct. The correct answer is Yoda. You lost {score} point(s) .\n")
    print(f"Your score is now: {score}.\n")

print("Let's keep it going!\n")
print("Question 3: What is baby Yoda's real name?\n")
answer_3 = input()

if (answer_3.lower() == "Grogu".lower()):
    score += 1
    print(f"/nYou are on fire! You got it right! You earned have {score} point(s).\n")
    print(f"Your score is now: {score}.\n")
else:
    score -= 1
    print(f"\nOpe. Sorry that is not the right answer. The correct answer is Grogu. You lost {score} point(s).\n")
    print(f"Your score is now: {score}.\n")

print("Let's get into some more questions!\n")
print("Question 4: Who is Palpatine's grandaughter?\n")
answer_4 = input()

if (answer_4.lower() == "Rey".lower()):
    score += 1
    print(f"\nYou are correct, my apprentice..You earned {score} point(s)\n")
else:
    score -= 1
    print(f"\nYou have failed me for the last time. The correct answer is Rey. You lost {score} point(s).\n")


print("Wow! You've made it so far! Let's keep going!\n")
print("Question 5: Who killed Qui-Gon Jinn?\n")
print("Hint: This one is kind of hard, but the killer looks the demon dude from Insidious\n")
answer_5 = input()

if (answer_5.lower() == "Darth Maul".lower()):
    score += 1 
    print(f"\nYou are correct!. You earned {score} point(s).\n")
    print(f"Your score is now: {score}.\n")
else:
    print(f"\nOoo. Better luck next time, the correct answer was Darth Maul. You lost {score} point(s).\n")
    print(f"Your score is now: {score}.\n")

print("Alright, next question!\n")
print("Question 6: Who was the Queen of Naboo and also served as a senator on the Galactic Senate?\n")
answer_6 = input()

if (answer_6.lower() == "Padme Amidala".lower()):
    score += 1
    print(f"\nYou got it right, great job! You have earned {score} point(s).\n")
    print(f"Your score is now: {score}.\n")
else:
    score -= 1
    print(f"\nSorry that answer is not correct. The correct answer is Padme Amidala. You have lost {score} point(s).\n")
    print(f"Your score is now: {score}.\n")

print("Next question!\n")
print("Question 7: Which actor played Luke Skywalker?\n")
answer_7 = input()

if (answer_7.lower() == "Mark Hamill".lower()):
    score += 1
    print(f"\nWoo! That is correct! You have earned {score} point(s)\n ")
    print(f"Your score is now: {score}.\n")
else:
    score -= 1 
    print(f"\nSorry that answer is not correct. The correct answer is Mark Hamill. You lost {score} point(s).\n")
    print(f"Your score is now: {score}.\n")

print("We are almost at the end of the quiz, only 2 more questions left!\n")
print("Question 8:  What character did Carrie Fisher's daughter Billie Lourd play in Star Wars?\n")
answer_8 = input()

if (answer_8.lower() == "Lieutenant Kaydel Connix".lower()):
    score +=1
    print(f"\nYes! You got it! You have earned {score} point(s).\n")
    print(f"Your score is now: {score}.\n")
else:
    score -= 1
    print(f"\nNOPE! Wrong answer, the correct answer was Lieutenant Kaydel Connix. You lost {score} point(s).")
    print(f"Your score is now: {score}.\n")


print("Alright, after this, there is only one more question left!\n")
print("Question 9:  Lightsabers are powered by what type of crystal?\n")
answer_9 = input("\n")

if (answer_9.lower() == "Kyber crystal".lower()):
    score += 1 
    print(f"\nYes! You got it! You have earned {score} point(s).")
    print(f"Your score is now: {score}.\n")
else:
    score -= 1
    print(f"\nOops, that was not correct. The correct answer is kyber crystal. You have lost {score} point(s)\n")
    print(f"Your score is now: {score}.\n")

print("Okat this is the last question...\n")
print("Question 10:  Who is the black market droidsmith Poe knows on Kijimi?\n")
answer_10 = input("\n")

if (answer_10.lower() == "Babu Frik".lower()):
    score += 1
    print(f"\nYes! You got it! You have earned {score} point(s). ")
    print(f"Your score is now: {score}.\n")
    
else:
    score -= 1
    print(f"\nOof. Better luck next time kid, that was the wrong answer. The correct answer is Babu Frik. You have lost {score}")
    print(f"Your score is now: {score}.\n")
    

print(f"You did it, you completed the quiz!/n")
print(f"Your final score is: {score}/n")

if score == 10:
    print("You got all of the questions right! Good Job!")
elif score < 10:
    print(f"Good try, you still did great! You got {score} out 10 questions right! Your final score was {score} point(s), better luck next time!")

print("Thank you for playing and take care!")



# need to find a way to keep score in the game
# score counter would look like: score = 0, if the answer
# maybe create another variable for the decreased score so that the math is done properly by the program, like lost_point = score - 1
