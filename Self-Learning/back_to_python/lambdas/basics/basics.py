# A regular named function
def square(num): return num * num

# An equivalent lambda, saved to a variable but has no name
square2 = lambda num: num * num

# Another lambda --> anonymous function
add = lambda a,b: a + b #automatically returns

#Executing the function
print(square(7))
# Executing the lambdas
print(square2(7))
print(add(3,10))

# Notice that the square function has a name, but the two lambdas do not
print(square.__name__)
print(square2.__name__)
print(add.__name__)


#Adding 
add_values = lambda x, y: x + y

#Multiplying 
multiply_values = lambda x, y: x * y

#dividing 
divide_values = lambda x, y: x / y


#subtract  
subtract_values = lambda x, y: x - y

# Cube 
cube = lambda a: a ** 3

print(cube(8))