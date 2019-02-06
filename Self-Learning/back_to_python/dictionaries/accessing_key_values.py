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

print(sample)

sample_name = instructor['name']  # if not found will print keyerror
print(sample_name)
age = "age"
print(instructor[age])

artist = {
    "first": "Neil",
    "last": "Young",
}
first_name = artist['first']
last_name = artist['last']
full_name = first_name + " " + last_name
fullName = f'{first_name} {last_name}'