# is_odd_string
# # Write a function called is_odd_string which returns true if sum of each character's position in the alphabet is odd. For example, "a" is in the first position,  "b" is in the second position, and so on. If the sum is even, return false.
# note: INDEXING STARTS AT 1.  A is position 1,
# NOT POSITION 0.


def is_odd_string(word):
    # 0 at index 0 because a is supposed to start at index 1
    alphabet = "0abcdefghijklmnopqrstuvwxyz"
    temp_generator = (alphabet.index(char) for char in word)
    return sum(temp_generator) % 2 != 0

# Test Cases
print(is_odd_string('a'))  # True
print(is_odd_string('aaaa'))  # False
print(is_odd_string('amazing'))  # True
print(is_odd_string('veryfun'))  # True
print(is_odd_string('veryfunny'))  # False
