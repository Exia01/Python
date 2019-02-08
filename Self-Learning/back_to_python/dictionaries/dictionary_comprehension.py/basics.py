
creator = {
    'title': 'patagonia bus',
    'author': 'Kal DJ',
    'songs': [
        {'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
        {'title': 'song2', 'artist': [
            'kitty', 'djcat'], 'duration': 5.25},
        {'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
    ],
    'instructor': [{
        'name': 'John',
        'has_pets': False,
        'age': 18,
        'favorite_language': 'Python',
        'favorite_color': 'Purple',
        'favorite_sport': 'Soccer!',
        'test': [1, 2, 3, 4, 5],
    }]
}

numbers = dict(
    first=1,
    second=2,
    third=3
)

squared_numbers = {key: value ** 2 for key, value in numbers.items()}
# loops through and manipulates the value
print(squared_numbers)
arr = [1, 2, 3, 4]
new_dict = {num: num ** 2 for num in arr}  # creates dictonary

letters = "ABC"
numbers_strings = "123"

combo = {letters[i]: numbers_strings[i] for i in range(0, len(letters))}
print(combo)

sample = dict(name='John',
              favorite_language='Python',
              favorite_color='Purple',
              favorite_sport='Soccer!',)

all_upper = {key.upper(): value.upper() for key, value in sample.items()}
print(all_upper)
