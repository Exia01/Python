# We can pass funcs as args to other funcs

def sum(n, func):
	total = 0
	for num in range(1,n+1):
		total += func(num)
	return total

def square(x):
	return x*x

def cube(x):
	return x*x*x

def half(x):
	return x/2


#sum either a cube
print(sum(3,cube)) #passing cube function
print(sum(3,square))
print(sum(4,half))

