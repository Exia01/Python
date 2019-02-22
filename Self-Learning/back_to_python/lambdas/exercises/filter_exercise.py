# write a function called "remove_negatives" that accepts a list of numbers and returns a copy of the list with all negative numbers removed


def remove_negatives(l):
    return list(map(lambda n: n, filter(lambda x: x >= 0, l)))

# Test cases


print(remove_negatives([-1, 3, 4, -99]))
print(remove_negatives([-1, 0, 1, 2, 3, 4, 5]))
print(remove_negatives([50, 60, 70]))


# Another way:
def _remove_negatives(nums):
    return list(filter(lambda l: l >= 0, nums))

# Test cases


print(_remove_negatives([-1, 3, 4, -99]))
print(_remove_negatives([-1, 0, 1, 2, 3, 4, 5]))
print(_remove_negatives([50, 60, 70]))
