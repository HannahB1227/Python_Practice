import sys
from random import *

print("Guess the Number")
print("Instructions: ")
print("\tEnter a guess between 0 and 100")
print("\tKeep guessing until you are correct or enter exit to end the game\n")
number = randint(0,100)
count = 0
while True:
    answer = input("Guess a number: ")
    if answer.isdigit():
	    if int(answer) < number:
		    print("Your guess is too low! Try again!")
		    count+=1
	    elif int(answer) > number:
		    print("Your guess is too high! Try again!")
		    count+=1
	    else: 
		    print("You're correct!")
			count+=1
		    print("It took you " + str(count) + " guesses.")
		    break
    else:
	    print("Your guess needs to be a number! Try again!")
sys.exit()