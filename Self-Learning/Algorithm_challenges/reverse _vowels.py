# reverse_vowels
# Write a function called reverse_vowels. This function should reverse the vowels in a string. Any characters which are not vowels should
# remain in their original position. You should not consider "y" to be a vowel.


def reverse_vowels(sentence):
    vowels = "aeiou"
    letter_stack = []
    for letter in sentence:
        if letter.lower() in vowels:
            letter_stack.append(letter)
    # advise: Don't modify strings. Work with them as lists; turn them into strings only when needed.
    result_string = "".join(
        (letter_stack.pop() if l.lower() in vowels else l for l in sentence)
    )
    return result_string


# #test Cases
print(reverse_vowels("Hello!"))  # "Holle!"
print(reverse_vowels("Tomatoes"))  # "Temotaos"
"RivArsI Vewols en e Streng"
print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("aeiou"))  # "uoiea"
print(reverse_vowels("why try, shy fly?"))  # "why try, shy fly?"


# https://stackoverflow.com/questions/529424/traverse-a-list-in-reverse-order-in-python
# using reversed due to lower memory usage no "isslice" needed
"""https://stackoverflow.com/questions/6295185/looping-through-a-list-from-a-specific-key-to-the-end-of-the-list  """
