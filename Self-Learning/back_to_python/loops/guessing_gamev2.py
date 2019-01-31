import random

def generaterandom():
    random_number = random.randint(1, 10)  # numbers 1 - 10
    return random_number

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low
tries = 1
def guessingGame(generaterandom, tries):
    print("Guess the number.. 1 - 10! Whole Numbers only.")
    random_number = generaterandom()
    while random_number:
        guess_number = int(input())
        # print(f'{tries} out of 5 tries')
        if random_number == guess_number:
            print("You Won!")
            play_again = input("Do you want to play again? (y/n) ")
            if play_again == "y":
                random_number = random.randint(1,10)  # numbers 1 - 10
                guess_number = None
            else:
                print("Thank you for playing!")
                break
        elif guess_number > random_number:
            state = "Too High, try again!"
        else:
            state = "Too low, try again!"
        print(state)
        tries += 1
        if tries == 6:
            print('Ran out of tries :(')
            break

guessingGame(generaterandom, tries)


# BONUS - let player play again if they want!
""" print("Would you like to play again?")
replay = input()

try:
    replay == "Yes"
    guessingGame(random_number, tries)
except:
    print("Well thanks for playing!") """