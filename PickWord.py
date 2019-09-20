import sys
import random

def pick_word():
    words = []
    with open("sowpods.txt", "r") as open_file:
	    words = open_file.readlines()
	    word = random.choice(words)
    return word

print("Random word is: " + pick_word())
sys.exit()