import sys
import random

def rand_list():
    list = random.sample(range(1,25), 10)
    print(list)
    return list

def get_ends(list):
    result = [list[0], list[len(list)-1]]
    return result
	
print(get_ends(rand_list()))
sys.exit()