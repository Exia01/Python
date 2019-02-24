#write a function called sum_floats
#This function should accept a variable number of arguments.
#Should return the sum of all the parameters that are floats.
# if the are no floats return 0

def sum_floats(*args):
    if (any(type(val) == float for val in args)):
        return sum((val for val in args if type(val)==float))
    return 0
#Test Cases

print(sum_floats(1.5, 2.4, 'awesome', [], 1))# 3.9
print(sum_floats(1,2,3,4,5))# 0 