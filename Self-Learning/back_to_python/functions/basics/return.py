number = 9

def print_square_number(number):
    number ** 2 
    #this does not return anything so nothing will be sent out
    

print_square_number(number)

nums = [1, 2, 3, 4]


def print_square_of_7(): #This function does not return anything
	print(7**2)

print_square_of_7()

def square_of_7(): 
	print("I AM BEFORE THE RETURN!")
	return 7**2
	print("I AM AFTER THE RETURN!")

result = square_of_7()
print(result)

# return 101s, 
# will exit the function
# https://www.cs.ucsb.edu/~pconrad/cs8/topics.beta/theStack/02/