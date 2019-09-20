import sys

num = int(input("Enter a number: "))
check = int(input("Enter a second number: "))
if num%4 == 0:
    print(str(num) + " is a multiple of 4.")
elif num%2 == 0:
    print(str(num) + " is an even number.")
else:
    print(str(num) + " is an odd number.")
if num%check == 0:
    print(str(num) + " is divisible by " + str(check))
else:
    print(str(num) + " is not divisible by " + str(check))
sys.exit()