import sys

print("Rock-Paper-Scissors\n")
while True:
    p1 = input("Player 1: Rock, Paper, or Scissors? ").lower()
    p2 = input("Player 2: Rock, Paper, or Scissors? ").lower()
    if ((p1 == "scissors") and (p2 == "paper")) or ((p1 == "paper") and (p2 == "rock")) or ((p1 == "rock") and (p2 == "scissors")):
	    print("Player 1 wins!")
    elif p1 == p2:
        print("It's a tie!")
    else:
        winner = 2
        print("Player 2 wins!")
    r = input("Would you like to play again? ")
    if r.lower() == "no":
	    print("Goodbye!")
	    break
sys.exit()