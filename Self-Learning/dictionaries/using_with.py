# does a dictionary have a key?
instructor = {
    'name': 'John',
    'has_pets': False,
    'age': 18,
    'favorite_language': 'Python',
    'favorite_color': 'Purple',
    'favorite_sport': 'Soccer!',
    'test': [1, 2, 3, 4, 5],
}

print("name" in instructor)  # True
print(1 in instructor['test'])  # True

if 18 in instructor.values():
    print("Perform action here")
    print(type(instructor.values()))
if [1, 2, 3, 4, 5] in instructor.values():
    # picks up whole object but not individual values
    print("Perform action here")
    print(type(instructor.values()))
