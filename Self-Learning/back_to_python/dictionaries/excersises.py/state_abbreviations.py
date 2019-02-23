# covert two list to

abbreviations = ["CA", "NJ", "RI"]
states = ["California", "New Jersey", "Rhode Island"]
if len(abbreviations) != len(states):
    raise Exception('Not the same length')

combination = {states[i]: abbreviations[i] for i in range(0, len(abbreviations))}
print(combination)


#using Zip
#https://www.programiz.com/python-programming/methods/built-in/zip

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
print(list(zip(list1, list2)))
x = dict(zip(list1, list2))
print(x)
