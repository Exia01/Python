# Write a function called nth, which accepts a list and a number and returns the element at whatever index is the number in the list. If the
# number is negative, the nth element from the end is returned.
# You can assume that number will always be between the negative value of the list length, and the list length minus 1.

def nth(list, num):
    return(list[num])

#Test Cases
print(nth(['a', 'b', 'c', 'd'], 1))  # 'b' 
print(nth(['a', 'b', 'c', 'd'], -2)) #  'c'
print(nth(['a', 'b', 'c', 'd'], 0))  # 'a'
print(nth(['a', 'b', 'c', 'd'], -4)) #  'a'
print(nth(['a', 'b', 'c', 'd'], -1)) #  'd'
print(nth(['a', 'b', 'c', 'd'], 3))  # 'd'