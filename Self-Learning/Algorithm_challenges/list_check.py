# Write a function called list_check, which accepts a list and returns True if each value in the list is a list. Otherwise the function should
# return False.

def list_check(val_list):
    return all((isinstance(val, list) for val in val_list))

# Test Cases
print(list_check([[],[1],[2,3], (1,2)])) # False
print(list_check([1, True, [],[1],[2,3]])) # False
print(list_check([[],[1],[2,3]])) # True