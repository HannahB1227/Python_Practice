import sys
import random

print("Guessing Game")
print("Type quit to exit the game\n")
cont = true
while cont:
    number = random.randint(1,9)
    count = 0
    while True:
	    answer = input("Guess the number between 1 and 9: ")
	    count+=1
	    if answer == "quit":
		    print("Goodbye!")
		    break
	    elif int(answer) == number:
		    print("You're correct!")
		    print("It took you " + str(count) + " guess(es) to win.")
		    break
	    else:
		    print("That's not right. Try again.")
    resp = input("Would you like to play again? ")
    if resp == "no"
	    cont = false
sys.exit()