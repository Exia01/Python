""" This Version features a computer version """
from random import randint # more explicit; not needed just minor

print("...rock...")
print("...paper...")
print("...scissors...")
choices = ['rock', 'paper', 'scissors']
rand_num = randint(0, len(choices)-1)

print("(Enter your choice):")
player = input()
print('*** No Cheating!!! ***')
print(' \n' * 25)
computer = choices[rand_num]
print("SHOOT!")

player = player.lower()


def gameON(player=None, computer=None):
    print(f'Computer plays {computer}')
    if player == computer:  # first check, if true the rest won't run
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("Player wins!")
        # we already ruled out every every possibility so else is fine
        else:
            print("Computer wins!")
    elif player == "paper":
        if computer == "rock":
            print("Player wins!")
        else:
            print("Computer wins!")
    elif player == "scissors":
        if computer == "paper":
            print("Player wins!")
        else:
            print("Computer wins!")
    else:
        print("Please enter a valid move")


gameON(player, computer)
