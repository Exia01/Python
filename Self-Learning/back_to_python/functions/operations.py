# addd
def add(a, b):
    return a+b


print(add(5, 6))


# divide
def divide(num1, num2):  # num1 and num2 are parameters
    return num1/num2


print(divide(2, 5))  # 2 and 5 are the arguments
print(divide(5, 2))


# square
def square(num):  # takes in an argument
    return num * num


print(square(4))
print(square(8))



#return examples 
def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
        return total  # Returning too early :(
# OLD-VERSION----OLD-VERSION----OLD-VERSION-----


# NEW AND IMPROVED VERSION :)
def sum_odd_numbers_2(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total


print(sum_odd_numbers_2([1, 2, 3, 4, 5, 6, 7]))


# cleaner code example
def is_odd_number(num):
    if num % 2 != 0:
        return True
    else:  # This else is unnecessary
        return False


def is_odd_number_2(num):
    if num % 2 != 0:
        return True
    return False  # We can just return without the else


print(is_odd_number_2(4))
print(is_odd_number_2(9))


def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count

print(count_dollar_signs("$uper $size"))