import sys

def get_number():
    number = int(input("How many Fibonacci numbers to calculate? "))
    return number

def get_Fibonacci(x):
    count = 2
    n1 = 1
    n2 = 1
    if x == 1:
	    list = [n1]
    else:
	    list = [n1, n2]
    while count < x:
	    n = n1 + n2
	    list.append(n)
	    count+=1
	    n1 = n2
	    n2 = n
    return list

print(get_Fibonacci(get_number()))
sys.exit()