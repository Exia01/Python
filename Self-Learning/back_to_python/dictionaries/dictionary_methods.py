
import random
sample = dict(name='John',
              has_pets=False,
              age=18,
              favorite_language='Python',
              favorite_color='Purple',
              favorite_sport='Soccer!',
              test=[1, 2, 3, 4, 5],)

# copy
sample_two = sample.copy()  # makes a copy of the dictionary
sample is sample_two  # false because of memory allocation
sample == sample_two  # True equality of values not memory


# create a dictionary
# fromkeys --> creates a key-value pairs from comma separated values:
x = {}.fromkeys("a", "b")
y = {}.fromkeys("a", [1, 2, 3, 4, 5])
print(x)
print(y)


new_user = {}.fromkeys(([]))
# without parenthesis will try to loop each string
new_user = {}.fromkeys(['name', 'score', 'email', 'profile bio'], 'unknown')
print(new_user)

numbers_dictionary = {}.fromkeys(range(1, 10), 'unknown')
print(numbers_dictionary)

# get --> retrieves value for a key or none if not there.
print(sample.get('test'))
print(sample.get('the_waahht'))  # none


# clear
sample.clear()  # will clear keys and values the dictionary
# print(sample)
