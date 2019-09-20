import sys
import random

def remove_dups(list):
    r = []
    r = [x for x in set(list) if x not in set(r)]
    return r

a = [1, 3, 5, 2, 6, 3, 6, 7, 1, 9]
print(a)
print(remove_dups(a))
sys.exit()