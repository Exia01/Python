# double_return
# Write a function called double_return which accepts a function and returns another function. double_return should decorate a function
# by returning two copies of the inner function's return value inside of a list.


'''
@double_return 
def add(x, y):
    return x + y
    
add(1, 2) # [3, 3]

@double_return
def greet(name):
    return "Hi, I'm " + name

greet("Colt") # ["Hi, I'm Colt", "Hi, I'm Colt"]
'''
from functools import wraps


def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):  # passing args from the function
        function_1 = fn(*args)
        # print([function_1, function_1])
        return [function_1, function_1]
    return wrapper


@double_return
def greet(name):
    return "Hi, I'm " + name


@double_return
def add(x, y):
    return x + y


# Test Cases
add(1, 2)  # [3, 3]
greet("Colt")  # ["Hi, I'm Colt", "Hi, I'm Colt"]


# optimized way of doing it
def double_return(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper
