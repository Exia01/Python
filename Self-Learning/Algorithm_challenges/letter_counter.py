# Write a function called letter_counter which accepts a string and returns a function. When the inner function is invoked it should accept a parameter which is a letter, and the inner function should return the number of times that letter appears. This inner function should be
# case insensitive.
def letter_counter(word):
    word = word.lower()
    # Storing keys(letters) and count | l short for letter
    temp_dictionary = {l: word.count(l) for l in word}
    def temp_function(letter):
        return temp_dictionary.get(letter, 0)
    return temp_function


#Test Cases 

counter = letter_counter('Amazing')
print(counter('a')) # 2
print(counter('m')) # 1

counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1 