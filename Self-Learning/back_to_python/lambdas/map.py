# map is a standard function that accepts two or arguments, a function and an iterable(list, string, dictionary, tuple or set)

# runs a lambda for each value in the iterable and returns a map object which can be converted into another data structure

# Example 1
nums = [2, 4, 5, 8, 10]

# this will loop through each number in the nums list
doubles = map(lambda x: x * 2, nums)
print(doubles)  # map object --> can only be iterated once
new_list = list(doubles)
print(new_list)
print(list(doubles))  # empty or None

# Example 2
doubles_ = list(map(lambda x: x * 2, nums))
print(doubles_)

# Example 3
people = ["Darcy", "Christina", "Dana", "Anabel"]

upperCasePeeps = map(lambda name: name.upper(), people)
print(list(upperCasePeeps))

# Example 4
names = [
    {'first': 'Jose', 'last': 'Gonzalez'},
    {'first': 'Batman', 'last': None},
    {'first': 'Alexander', 'last': 'Rodriguez'},
]
first_names = list(map(lambda x: x['first'], names))
print(first_names)
