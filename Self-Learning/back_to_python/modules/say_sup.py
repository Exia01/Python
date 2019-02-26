# special properties that exists. Don't mess with them!
def say_sup():
    print(f'Hi my __name__ is {__name__}')

if __name__ == "__main__":
    say_sup()  # prints 3 things. that's weird
