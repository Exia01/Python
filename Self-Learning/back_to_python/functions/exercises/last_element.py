# Write a function called "last_element"
# Function takes in one parameter -> list and returns the last value in the list. Should return None if empty


def last_element(*args):
    obj = args[0]
    if not args:
        return None
    if type(obj) != list:
        return "Argument must be a list"

    try:
        result = obj.pop()
    except IndexError:
        return None
    return result


# Much Simpler way:
def last_element_refractor(l):
    if l:
        return l[-1]
    return None

#Variables
sample_1 = {
    'a': [1, 2, 4, 5, 6]
}
sample_2 = [1, 2, 3, 4, 5, 6]

# testCases

print(last_element(sample_1))  # test case1
print(last_element(sample_2))  # test case2
print(last_element_refractor(sample_2))  # test case2
