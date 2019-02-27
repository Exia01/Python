# Create a function "frequency"
# Function accepts a 'list' and a 'search_term'


def frequency(list=None, search_term=None):
    if not list or not search_term:
        return None
    return list.count(search_term)


# Test Cases
list = [1, 2, 4, 5, 6, 6, 7, 8, 4, 4, 4]
search_term = 4

print(frequency(list, search_term))

# multiply_even
# Create a function that accepts a list of numbers, returns the sum of multiplied even number


def multiply_even_numbers(list=None):
    total = 1
    for num in list:
        if num % 2 == 0:
            total *= num
    return total


print(multiply_even_numbers([2, 3, 4, 5, 6]))

#capitalize 
#create a function that capitalizes the first letter of a word
def capitalize(word=None):
    if word:
        return word.capitalize()

print(capitalize("tim"))
print(capitalize("matt"))

#another way
def capitalize_2(string):
    return string[:1].upper() + string[1:]  #separate and put back together
    
#Intersection 
#write a function "intersection" should accept two list and return a new one with the values in both
def intersection(list_1, list_2):
        result = [value for value in list_1 if value in list_2]
        return result
# not so sure about this one but it is using sets
def intersection_2(list1, list2):
    return [val for val in set(list1) & set(list2)]

print(intersection_2([1,3,4,5],[23,5,4,5]))