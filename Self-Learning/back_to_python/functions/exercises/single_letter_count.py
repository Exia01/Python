# Write a function called "single_letter_count" This function takes in two parameters
# The first parameter should be a word and the second should a letter
# Function should be case insensitive if no letter have been found the function should return 0


def single_letter_count(word=None, letter=None):
    if not word and not letter:
        return 0
    if word and letter:
        letter = letter.lower()
        return word.lower().count(letter)
    return 0
 
 #variables
word1, word2 = "Hello Another one Outthere", 'WORLD CaliForniaBeauty! :D'
letter1, letter2 = "t", 'b'

#Test cases
print(single_letter_count(word1, letter1))
print(single_letter_count(word2, None))