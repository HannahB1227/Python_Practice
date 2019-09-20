import sys

name = input("Enter your name: ")
print("Your name is " + name)
age = input("Enter your age: ")
print("You are " + age + " years old.")
statement = name + ", you will be 100 years old in " + str(100-int(age)) + " years. It will be the year " + str((2018 - int(age)) + 100) + ". "
print(statement)
copies = input("Enter a number: ")
count = 0
print(int(copies) * statement)
print("\nSorry about that. Does this look better?")
print(int(copies) * (statement + "\n"))
sys.exit()