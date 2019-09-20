import sys
from random import *

while True:
    answer = input("Would you like to roll the dice? ")
    if answer.rfind("yes") != -1:
        print(randint(1,6))
    elif answer.rfind("no") != -1:
	    print("Goodbye!")
	    break
    else:
        print("Response not accepted. Try again.")
sys.exit()