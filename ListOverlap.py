import sys
import random

list1 = []
list2 = []
list1 = random.sample(range(1,50), 10)
list2 = random.sample(range(1,50), 13)
print(list1)
print(list2)
print("The overlap of the lists is: ")
print(list(set(list1) & set(list2)))
sys.exit()