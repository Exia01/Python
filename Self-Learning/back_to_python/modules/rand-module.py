""" Only import what you need!!  """
from random import choice as pick, randint as magic_number_chooser


# we can rename them 
print(pick(["apple", "banana", "cherry", "durian"]))
print(magic_number_chooser(1,100))


from random import (choice, randint, shuffle as mix)
#Without naming
print(choice(["apple", "banana", "cherry", "durian"]))
print(randint(1, 100))
x = ["apple", "banana", "cherry", "durian"]
mix(x)
print(x)