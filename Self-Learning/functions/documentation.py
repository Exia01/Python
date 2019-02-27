import random
def exponent(num, power=2):
	"""exponent(num, power)raises num to specified power. Power defaults to 2."""
	return num ** power

print(exponent(2,3)) #8
print(exponent(3)) #9
print(exponent(7)) #49

print(exponent.__doc__) # this wll print out he documentation inside exponent


print(random.randint.__doc__) # will print out the documentation from random module 



