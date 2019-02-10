# creating a set
sample = {x ** 2 for x in range(10)}
# do not have to pass key or value since it is a unique val
dictionary_sample = {x: x ** 2 for x in range(10)}
# very similar but the variable above will produce a dictionary

# set from string
greeting = "Hello World!"
word = "Sequoia Tree"
sample2 = {char.upper() for char in greeting}


print(sample)
print(sample2)

# as a function

def are_all_vowels_in_string(*test):
    print(test[0])
    temp = {char for char in x if char in 'aeiou'} 
    print(temp)
    return len({char for char in test[0] if char in 'aeiou'}) == 5


x ='Unfortunate Events'
print(are_all_vowels_in_string(word, x))