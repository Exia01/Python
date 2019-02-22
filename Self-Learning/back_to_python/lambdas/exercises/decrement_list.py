#Write a function that accepts a single list of numbers as a parameter.

#Should return a copy of the list where each item has been decremented by one. 

#Use map

def decrement_list(num_list):
    return list(map(lambda num: num-1, num_list))
print(decrement_list([1,2,3]))