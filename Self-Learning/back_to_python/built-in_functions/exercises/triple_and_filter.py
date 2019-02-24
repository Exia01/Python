# write a function called "triple_and_filter"
# This function should accept a list of numbers, filter out every number that is not divisible by 4, and return a new list where every remaining number is triple_and_filter


def triple_and_filter(l):
    if not l:
        return - 1
    return list(map(lambda val: val*3,(filter(lambda num: num % 4 == 0, l)))) 


# Test Cases
print(triple_and_filter([1, 2, 3, 4]))  # 12
print(triple_and_filter([6, 8, 10, 12]))  # 24, 36


#Explanation:
#Check if there is a list
# starting at the filter, we iterate running a lambda that will return numbers divisible by 4
# we then cycle through using a map, which runs a lambda on each value and multiplying by 3
# we then turn it into a list 


#refractored:
def _triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x * 3, lst)))
    
    #Multiply the numbers...then check and filter