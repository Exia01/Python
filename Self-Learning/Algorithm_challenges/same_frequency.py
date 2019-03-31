# Write a function called same_frequency which accepts two numbers and returns True if they contain the same frequency of digits.
# Otherwise, it returns False.


def same_frequency(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    temp_dict = {}
    for x in num2:
        try:
            temp_dict[x] += 1
        except KeyError:
            temp_dict[x] = 1
    for y in num1:
        if temp_dict.get(y, 0) == 0:
            return False
        else:
            temp_dict[y] -= 1
    return True

# Test Cases
print(same_frequency(551122, 221515))  # True
print(same_frequency(321142, 3212215))  # False
print(same_frequency(1212, 2211))  # True


#another way
def _same_frequency(num1,num2):
    d1 = {letter:str(num1).count(letter) for letter in str(num1)}
    d2 = {letter:str(num2).count(letter) for letter in str(num2)}
  
    for key,val in d1.items():
        if not key in d2.keys():
            return False
        elif d2[key] != d1[key]:
            return False
    return True