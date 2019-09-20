import sys

def max(x, y, z):
    if (x > y) and (x > z):
	    print(x)
    elif (y > x) and (y > z):
	    print(y)
    else:
	    print(z)

r = input("Enter three numbers: ").split()
x = int(r[0])
y = int(r[1])
z = int(r[2])
print("Max is: ", end="")
max(x, y, z)
sys.exit()