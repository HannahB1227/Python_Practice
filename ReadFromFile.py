import sys

def readFile(filename):
    lines = []
    with open(filename, 'r') as open_file:
	    for line in open_file:
		    if line.find("/") != -1:
			    vector = line.split("/")
			    lines.append(vector[2])
		    else:
			    lines.append(line.replace("\n", ""))
    return lines

def countElements(arrayAll, arraySet):
    dictionary = {}
    for e in arraySet:
	    dictionary[e] = arrayAll.count(e)
    return dictionary

def main(filename):
    list = readFile(filename)
    listSet = set(list)
    d = countElements(list, listSet)
    for pair in d.items():
	    print(pair)

file1 = "namesList.txt"
print("No Extra: namesList.txt")
main(file1)
file2 = "Training_01.txt"
print("\nExtra: Training_01.txt")
main(file2)
sys.exit()