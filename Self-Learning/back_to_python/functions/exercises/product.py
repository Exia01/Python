# write a function called product that accepts two parameters and returns the product of the two parameters(multiply them together)

def product(a=0, b=0):
    """Takes in two arguments and multiplies them. Defaults to 0 if no arguments are provided."""
    return a * b
    

print(product(2, 2))
print(product())
print(product.__doc__)