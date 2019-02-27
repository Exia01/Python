#Implement a function "is_all_strings"
#Function accepts a single iterable and returns True if it contains ONLY strings. Otherwise, it should return False

def is_all_strings(l):
    return all((type(val)== str for val in l))  #using generator expression instead of a comprehesion
    

#Test Cases
print(is_all_strings(['a','b','c'])) #True
print(is_all_strings([2,'a','b','c'])) #False
print(is_all_strings(['Hello', 'Goodbye'])) #True