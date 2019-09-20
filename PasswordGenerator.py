import sys
import random
import string

def make_password(strength):
    if strength == 1:
	    password = random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, 6)
    elif strength == 2:
	    password = random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, 8)
    else: 
	    password = random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, 10)
    return "".join(password)
	
strength = int(input("How strong do you want your password?\n1-Weak\n2-Medium\n3-Strong\n"))
print("Password: " + make_password(strength))
sys.exit()
