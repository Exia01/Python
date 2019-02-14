#Function called "multiple_letter_count" 
# return dictionary with count of each letter


def multiple_letter_count(word = None):
    if not word:
        return None
    
    if word:
        return {letter: word.count(letter) for letter in word if letter != " "}
        

#Variables 
test_1 = "Hello World!"
test_2 = "Gotta keep Pushing!"

#Test cases
print(multiple_letter_count(test_1))
print(multiple_letter_count(test_2))