# def divide(a,b):
# 	try:
# 		result = a/b # do we have a result
# 	except ZeroDivisionError:
# 		print("don't divide by zero please!")
# 	except TypeError as err: # we can throw/raise the built in error
# 		print("a and b must be ints or floats")
# 		print(err)
# 	else:
# 		print(f"{a} divided by {b} is {result}") # execute the logic if passing

#refractor we can combine the errors and put them in a tuple
def divide(a,b):
	try:
		result = a/b
	except (ZeroDivisionError, TypeError) as err:
		print("Something went wrong!")
		print(err)
	else:
		return (f"{a} divided by {b} is {result}")
	return '\nExiting....'


print(divide(1,2))
print(divide(1,'a'))
# print(divide(1,0))
