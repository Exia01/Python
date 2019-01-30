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
    guess_number = int(input())
    while random_number:
        print(f'{tries} out of 5 tries')
        if random_number == guess_number:
            print("You Won!")
            break
        elif guess_number > random_number:
            state = "Too High, try again!"
        else:
            state = "Too low, try again!"
        print(state)
        guess_number = int(input())
        tries += 1
        if tries == 5:
            break

guessingGame(generaterandom, tries)


print("Would you like to play again?")
replay = input()

try:
    replay == "Yes"
    guessingGame(random_number, tries)
except:
    print("Well thanks for playing!")


# BONUS - let player play again if they want!