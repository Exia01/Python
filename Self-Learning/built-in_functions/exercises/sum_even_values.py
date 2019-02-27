# write a function called "sum_even_values"
# function should accept a variable number of arguments and return the sum of all the arguments that are divisible by 2
# if there are no arguments divisible by 2 return 0


def sum_even_values(*args):
    return sum((val for val in args if val % 2 == 0))  # using generator


# Test Cases
print(sum_even_values(1, 2, 3, 4, 6))  # 12
print(sum_even_values(4, 2, 1, 10))  # 16
print(sum_even_values(1))  # 0


#refractored solution:
def R_sum_even_values(*arg):
    if arg:
        return sum(a for a in arg if a % 2 == 0)
    return 0