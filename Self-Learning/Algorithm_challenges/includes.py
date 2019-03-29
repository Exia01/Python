# Write a function called includes which accepts a collection, a value, and an optional starting index. The function should return True if the
# value exists in the collection when we search starting from the starting index. Otherwise, it should return False.
# The collection can be a string, a list, or a dictionary. If the collection is a string or array, the third parameter is a starting index for where to
# search from. If the collection is a dictionary, the function searches for the value among values in the dictionary; since objects have no sort
# order, the third parameter is ignored.

def includes(arg, search_param, index=None):
    if type(arg) is dict:
       return any((val == search_param for val in arg.values()))
    if index is None:
        index = 0
    return any((True for x in range(index,len(arg)) if arg[x] == search_param))

#Test Cases
print(includes([1, 2, 3], 1)) # True 
print(includes([1, 2, 3], 1, 2)) # False 
print(includes({ 'a': 1, 'b': 2 }, 1)) # True 
print(includes({ 'a': 1, 'b': 2 }, 'a')) # False
print(includes('abcd', 'b')) # True
print(includes('abcd', 'e')) # False