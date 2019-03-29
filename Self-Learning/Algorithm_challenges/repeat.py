# Write a function called repeat, which accepts a string and a number and returns a new string with the string passed to the function
# repeated the number amount of times.


def repeat(arg, multiplier):
    if multiplier is 0:
        return ""
    return arg * multiplier


# Test Cases
print(repeat('*', 3))  # '***'
print(repeat('abc', 2))  # 'abcabc'
print(repeat('abc', 0))  # ''

#Here be dragons
def _repeat(string, num):
    if (num == 0):
        return ''
    i = 0
    newStr = ''
    while (i < num):
        newStr += string
        i += 1
    return newStr