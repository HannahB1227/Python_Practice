import sys

def readFile(filename):
    lines = []
    with open(filename, 'r') as open_file:
	    lines = open_file.read().splitlines()
    return lines

def compareFiles(f1, f2):
    list = []
    for x in f1:
	    if x in f2:
		    list.append(int(x))
    return list
	
def main(file1, file2):
    f1 = readFile(file1)
    f2 = readFile(file2)
    print(compareFiles(f1, f2))

file1 = "primenumbers.txt"
file2 = "happynumbers.txt"
main(file1, file2)
sys.exit()