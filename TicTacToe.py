import sys

def printBoard(game):
    for x in range(0,3):
	    print(" " + (3 * "--- "))
	    for y in range(0,3):
		    print("| ", end="")
		    if game[x][y] == 1:
			    print("X ", end="")
		    elif game[x][y] == 2:
			    print("O ", end="")
		    else:
			    print("  ", end="")
	    print("|")
    print(" " + (3 * "--- "))
	
def checkDraw(game):
    for x in range(0,3):
	    for y in range(0,3):
		    if game[x][y] == 0:
			    return False
    return True
	
print("Tic-Tac-Toe\n")
game = [[0,0,0],[0,0,0],[0,0,0]]
printBoard(game)
end = False
p = 1
while end != True:
    r = input("Player " + str(p) + ": ").split()
    row = int(r[0])
    col = int(r[1])
    game[row][col] = p
    printBoard(game)
    for i in range(0,3):
	    if (game[0][i] == game[1][i] == game[2][i]) and (game[0][i] != 0):
		    end = True
		    print("Player " + str(p) + " wins!")
		    break
	    elif (game[i][0] == game[i][1] == game[i][2]) and (game[i][0] != 0):
		    end = True
		    print("Player " + str(p) + " wins!")
		    break
	    elif (game[0][0] == game[1][1] == game[2][2]) and (game[0][0] != 0):
		    end = True
		    print("Player " + str(p) + " wins!")
		    break
	    elif (game[0][2] == game[1][1] == game[2][0]) and (game[0][2] != 0):
		    end = True
		    print("Player " + str(p) + " wins!")
		    break
	    else:
		    end = False
    if checkDraw(game) == True:
	    print("It's a draw!")
	    break
    if p == 1:
	    p = 2
    else:
	    p = 1

sys.exit()