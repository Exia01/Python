from random import random

#random genrates a number between 0-1
print(random()) #generates a float
def flip_coin():
	if random() > 0.5:
		return "Heads"
	else:
		return "Tails"

print(flip_coin())

