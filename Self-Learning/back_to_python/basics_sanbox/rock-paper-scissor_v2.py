print("...rock...")
print("...paper...")
print("...scissors...")

print("(enter Player 1's choice):")
player1 = input()
print('*** No Cheating!!! ***')
print(' \n' * 25)
print("(enter Player 2's choice):")
player2 = input()
print("SHOOT!")
player1 = player1.lower()

player2 = player2.lower()


def gameON(player1=None, player2=None):
    if player1 == player2: # first check, if true the rest won't run
        print("It's a tie!")
    elif player1 == "rock":
        if player2 == "scissors":
            print("Player 1 wins!")
        if player2 == "paper":
            print("Player 2 wins!")
    elif player1 == "paper":
        if player2 == "rock":
            print("Player 1 wins!")
        elif player2 == "scissors":
            print("Player 2 wins!")
    elif player1 == "scissors":
        if player2 == "paper":
            print("Player 1 wins!")
        elif player2 == "rock":
            print("Player 2 wins!")
    else:
        print("Something went wrong")

gameON(player1, player2)
