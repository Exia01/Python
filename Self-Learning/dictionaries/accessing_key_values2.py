# this will not be order specific when extracting data.
instructor = {
    'name': 'John',
    'has_pets': False,
    'age': 18,
    'favorite_language': 'Python',
    'favorite_color': 'Purple',
    'favorite_sport': 'Soccer!',
    'test': [1, 2, 3, 4, 5],
}

# another way of creating dictionary
sample = dict(name='John',
              has_pets=False,
              age=18,
              favorite_language='Python',
              favorite_color='Purple',
              favorite_sport='Soccer!',
              test=[1, 2, 3, 4, 5],)


a = instructor.values()
for value in instructor.values():
    print(value)  # will print out all the values
for keys in instructor.keys():
    print(keys)  # will print out all the values

b = instructor.items()  # will print out a tuple list of keys and values 

for k, v in sample.items():
    print(k, v)