#Write a function called number_compare. Takes in two numbers and compares the two.
# Return wether the first or second is greater or both are equal

def number_compare(a=None, b=None):
    # print( not a or not b)
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"
     # if not a or not b:
    #     return "Please provide two values to compare"

#variables
a, b, c, d = 9, 2, 3, 4

#Test Cases

print(number_compare(a, b))
print(number_compare(c, d))