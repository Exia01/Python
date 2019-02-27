# Write a function called "is_palindrome"
# Function should take in a one parameter and return True or False


def is_palindrome(string=None):
    if not string:
        return None

    temp_array = []
    string.lower().split(" ")

    for word in string:
        temp_array.append(word)

    temp_array.reverse()
    compare = ''.join(char for char in temp_array)
    if compare == string:
        return True
    return False


# test cases
print(is_palindrome('testing'))  # False
print(is_palindrome('tacocat'))  # True
print(is_palindrome('hannah'))  # True
print(is_palindrome('robert'))  # False


#simpler more optimized way
# def is_palindrome_sample2(string):
#     return string == string[::-1]
def is_palindrome_sample2(string):
    stripped = string.replace(" ", "") # removes whitespace
    return stripped == stripped[::-1] #starts at end 


# test cases
print(is_palindrome_sample2('testing'))  # False
print(is_palindrome_sample2('tacocat'))  # True
print(is_palindrome_sample2('hannah'))  # True
print(is_palindrome_sample2('robert'))  # False
