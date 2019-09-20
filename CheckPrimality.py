import sys

def get_divisors(number):
    list = []
    for x in range(2, number):
	    if number%x == 0:
		    list.append(x)
    return list

num = int(input("Enter a number: "))
div = get_divisors(num)
if div == []:
    print(str(num) + " is a prime number!")
else:
    print(str(num) + " is not a prime number!")
sys.exit()

