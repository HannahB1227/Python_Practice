import sys

number = int(input("Enter a number: "))
list = []
for x in range(2, number):
    if number%x == 0:
	    list.append(x)
print("The divisors of " + str(number) + " are: ")
print(list)
sys.exit()