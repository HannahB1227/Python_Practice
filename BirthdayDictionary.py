import sys

bdayDictionary = {"Emily Green": 12/09/99, "Darren Green": 12/16/68, "Kathy Burke": 08/03/63}
print("Welcome to the birthday dictionary. We know the birthdays of: ")
print(bdayDictionary.keys())
name = input("Who's birthday do you want to look up?")
print(name + "'s birthday is " + str(bdayDictionary.get(name, "not available")))
sys.exit()