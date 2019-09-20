import sys

list1 = [4, 2, 1, 6, 7, 9, 20, 3, 5, 5]

print("Extra 1")
list2 = []
for x in list1:
    if x < 5:
	    list2.append(x)
print(list2)

print("\nExtra 2")
list2 = []
[list2.append(x) for x in list1 if x < 5]
print(list2)

print("\nExtra 3")
list2 = []
num = int(input("Enter a number: "))
for x in list1:
    if x < num:
	    list2.append(x)
print(list2)
sys.exit()