import sys

def get_string():
    s = input("Enter a long string: ")
    return s

def rev_string(s):
    s1 = s.split()
    s2 = " ".join([x for x in s1[::-1]])
    return s2

print(rev_string(get_string()))
sys.exit()