
# simple solution:
# If you have a list of pairs, you can very easily turn it into a dictionary using dict() 
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
easy = dict(person)
print(easy)

# easier way
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {k: v for k, v in person}
print(answer)

#wordy 

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
person_profile = {num[0]: num[1] for num in person}

print(person_profile)


# using yield
#https://stackoverflow.com/questions/1747817/create-a-dictionary-with-list-comprehension-in-python

def key_value_gen(item):
   yield (item[0])
   yield (item[1])
   
testing = dict(map(key_value_gen, person))
print(testing)


# easier way
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {k: v for k, v in person}
print(answer)