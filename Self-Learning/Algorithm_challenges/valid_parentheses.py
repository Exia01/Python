# valid_parentheses
# Write a function called valid_parentheses that takes a string of parentheses, and determines if the order of the parentheses is valid.
# valid_parentheses should return true if the string is valid, and false if it's invalid.


def valid_parentheses(string):
    temp_stack = []
    results = []
    valid_dict = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    if len(string) < 2:
        return False
    for bracket in string:
        if bracket in valid_dict:
            temp_stack.append(valid_dict[bracket])
            # add the actual pair bracket
        elif not temp_stack or bracket != temp_stack.pop():
            return False
    return True


# Test Cases


print(valid_parentheses("{[[()]]}"))  # True
print(valid_parentheses(")(()))"))  # False
print(valid_parentheses("("))  # False
print(valid_parentheses("(())((()())())"))  # True
print(valid_parentheses('))(('))  # False
print(valid_parentheses('())('))  # False
print(valid_parentheses('()()()()())()('))  # False


# Here be dragons
# if len(string) % 2 != 0:
#     return False
# temp_dict = {key: string.count(key)
#                                for key in string if key in valid_dict.keys()}
# print(temp_dict)


#refractored