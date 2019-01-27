print("...rock...")
print("...paper...")
print("...scissors...")

print("(enter Player 1's choice):")
player1 = input()
print("(enter Player 2's choice):")
player2 = input()
print("SHOOT!")


if player1 == "rock" and player2 == "scissors":
    print("Player 1 wins!")
elif player1 == "rock" and player2 == "paper":
    print("Player 2 wins!")
elif player1 == "paper" and player2 == "rock":
    print("Player 1 wins!")
elif player1 == "paper" and player2 == "scissors":
    print("Player 2 wins!")
elif player1 == "scissors" and player2 == "rock":
    print("Player 2 wins!")
elif player1 == "scissors" and player2 == "paper":
    print("Player 1 wins!")
elif player1 == player2:
    print("It's a tie!")
else:
    print("Something went wrong")
