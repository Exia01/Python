# Return True if all elements of the iterable are truthy(or if the iterable is empty
# )

print(all([0, 1, 2, 3]))

#these run list comprehension and then analysis 
print(all([char for char in 'eio' if char in 'aeiou']))
print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

#example
people = ['Charlie', 'Casey', 'Cody', 'Carly', 'Christina']
result = [name[0] == 'C' for name in people]
print(result)
print(all(result))

#example 2

nums = [2, 30, 60, 26, 18]
nums_result = [num % 2 == 0 for num in nums] # we could wrap all around this 
print(nums_result)
print(all(nums_result))

# Any --> returns True if any element of the iterable is truthy. if the iterable is empty, return False
any([0, 1, 2, 3])  #True

any([val for val in [1,2,3] if val > 2]) # True
any([val for val in [1, 2, 3] if val > 5])  # False

nums = [2, 30, 60, 26, 18,21]
nums_result = [num % 2 == 1 for num in nums]
print(nums_result)
print(any(nums_result))