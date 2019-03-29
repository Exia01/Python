# Write a function called vowel_count that accepts a string and returns a dictionary with the keys as the vowels and values as the count of
# times that vowel appears in the string


def vowel_count(string):
    abc = "aeiou"
    result_dict = {}
    for letter in string.lower():
        if letter in abc:
            try:
                result_dict[letter] += 1
            except KeyError:
                result_dict[letter] = 1
    return result_dict


# Test Cases
print(vowel_count('awesome'))  # {'a': 1, 'e': 2, 'o': 1}
print(vowel_count('Elie'))  # {'e': 2, 'i': 1}
print(vowel_count('Colt'))  # {'o': 1}

#another way of doing it
def _vowel_count(string):
    lower_s = string.lower()
    return {letter: lower_s.count(letter) for letter in string if letter in "aeiou"}