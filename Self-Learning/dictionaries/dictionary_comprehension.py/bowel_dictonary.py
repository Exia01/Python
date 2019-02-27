# create a dictionary with "aeiou" as keys and values of 0

abc = "aeiou"
value = 0

sample = {letter: 0 for letter in abc}
print(sample)


# another way 
answer = dict.fromkeys("aeiou", 0)
print(answer)