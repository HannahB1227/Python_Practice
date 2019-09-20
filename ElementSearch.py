import sys
import random

def rand_list():
    list = sorted(random.sample(range(1,25), 10))
    print(list)
    return list

def get_num():
    return int(input("Enter a number: "))
	
def binary_search(list):
    num = get_num()
    first = 0
    last = len(list)
    found = False
    while (first <= last) and (found == False):
	    midpoint = int((last-first)/2)
	    if num > list[midpoint]:
		    first = midpoint+1
	    elif num < list[midpoint]:
		    last = midpoint-1
	    else: 
		    found = True
		    print(str(num) + " is in the list.")
		    break
    if found == False:
	    print(str(num) + " is not in the list.")

binary_search(rand_list())
sys.exit()