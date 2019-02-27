# special properties that exists. Don't mess with them!
from say_sup import say_sup


def say_hi():
    print(f'Hi my __name__ is {__name__}')


say_hi()  # this name variable is the default main
say_sup() 
