numbers = [1, 2, 3, 4, 5, 6, 7, 8]

evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]

print(evens)
print(odds)

another = [num * num if num % 2 == 0 else num / 2 for num in numbers]
print(another)

with_vowels = "I think I am getting the hang of it"

x = ''.join(char for char in with_vowels if char not in "aeiou")
print(x)