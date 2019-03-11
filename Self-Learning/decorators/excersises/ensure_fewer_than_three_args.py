# ensure_fewer_than_three_args
# Write a function called ensure_fewer_than_three_args which accepts a function and returns another function. The function passed to it
# should only be invoked if there are fewer than three positional arguments passed to it. Otherwise, the inner function should return "Too
# many arguments!"

'''
@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

add_all() # 0
add_all(1) # 1
add_all(1,2) # 3
add_all(1,2,3) # "Too many arguments!"
add_all(1,2,3,4,5,6) # "Too many arguments!"
'''

from functools import wraps


def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # print(len(args) > 2)
        if len(args) > 2:
            raise ValueError("Too many arguments!")
        return fn(*args, **kwargs)
    return wrapper


@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

#Test Cases
print(add_all())# 0
print(add_all(1))# 1
print(add_all(1,2))# 3
print(add_all(1,2,3))# "Too many arguments!"
print(add_all(1,2,3,4,5,6))# "Too many arguments!"