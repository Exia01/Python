""" This Version features a computer version """
from random import randint  # more explicit; not needed just minor


def gameON():
    computer_wins = 0
    player_wins = 0
    winning_score = 3
    while player_wins < winning_score and computer_wins < winning_score:
        print(f'Player score: {player_wins} Computer score: {computer_wins}')
        choices = ['rock', 'paper', 'scissors']
        rand_num = randint(0, len(choices) - 1)
        computer = choices[rand_num]
        print("...rock...")
        print("...paper...")
        print("...scissors...")

        print("(Enter your choice):")
        player = input()
        if player == "quit" or player == "q":
            break
        print('*** No Cheating!!! ***')
        print(' \n' * 25)
        print("SHOOT!")

        player = player.lower()

        print(f'Computer plays {computer}')
        if player == computer:  # first check, if true the rest won't run
            print("It's a tie!")
        elif player == "rock":
            if computer == "scissors":
                print("Player wins!")
                player_wins += 1
            # we already ruled out every every possibility so else is fine
            else:
                print("Computer wins! :o")
                computer_wins += 1
        elif player == "paper":
            if computer == "rock":
                print("Player wins!")
                player_wins += 1
            else:
                print("Computer wins! :o")
                computer_wins += 1
        elif player == "scissors":
            if computer == "paper":
                print("Player wins!")
                player_wins += 1
            else:
                print("Computer wins! :o")
                computer_wins += 1
        else:
            print("Please enter a valid move")
    if player_wins > computer_wins:
        print("Yay! you won!")
    elif player_wins == computer_wins:
        print('It\'s a tie!')
    else:
        print("Oh No! The computer won!")
    print(
        f'Final score!! --> Player score: {player_wins} Computer score: {computer_wins}')


gameON()
