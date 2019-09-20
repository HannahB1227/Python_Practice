import sys
import random

def main(low, high):
    count = 0
    while True:
	    num = random.randint(low, high)
	    count+=1
	    print(num)
	    r = input()
	    if r.lower() == "too low":
		    low = num+1
	    elif r.lower() == "too high":
		    high = num-1
	    elif r.lower() == "correct":
		    print("Congratulations! It took you " + str(count), end="")
		    if count < 2:
			    print(" try!")
		    else:
			    print(" tries!")
		    break
	    elif r.lower() == "quit":
		    print("Goodbye!")
		    break
	    else:
		    continue
	
print("Guessing Game Two")
main(0, 100)
sys.exit()