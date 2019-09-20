import sys

s1 = input("Enter a string: ")
s2 = ""
for x in reversed(s1):
    s2+=x
if s1.lower() == s2.lower():
    print("This is a palindrome!")
else:
    print("This is not a palindrome!")
sys.exit()