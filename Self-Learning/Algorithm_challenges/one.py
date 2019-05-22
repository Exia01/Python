# once
# Write a function called once. This function accepts a function and returns a new function that can only be invoked once. If the function is
# invoked more than once, it should return NONE
import collections


def once(func):
    once.count = 0
    def temp_function(num1, num2):
        once.count += 1
        if (isinstance(func, collections.Callable) and once.count < 2):
            return func(num1, num2)
        else:
            # print('Can only call once')
            return None
    return temp_function

#Test Cases
def add(a,b):
    return a+b

oneAddition = once(add)

print(oneAddition(2,2)) # 4
print(oneAddition(2,2)) # None
print(oneAddition(12,200)) # None