num_list = [1, 2, 3, 4]

odd_even = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}

print(odd_even)
sample = dict(name='John',
              favorite_language='Python',
              favorite_color='Purple',
              favorite_sport='Soccer!')

some_upper = {(key.upper() if key is 'name' else key): (value.upper() if value == "python" else value) for key, value in sample.items()}

print(some_upper)

