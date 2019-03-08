# get_multiples
# Write a function called get_multiples, which accepts a number and a count, and returns a generator that yields the rest count multiples of
# the number.
# The default number should be 1, and the default count should be 10.


def get_multiples(number=None, multiple_count=None):
    count = 0
    multiplier = 1

    if not multiple_count:
        multiple_count = 10

    if not number:
        number = 1

    while count < multiple_count:
        temp = number * multiplier
        yield temp
        count += 1
        multiplier += 1


default_multiples = get_multiples()
print(list(default_multiples))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = get_multiples(2, 3)
print(next(evens))  # 2
print(next(evens))  # 4
print(next(evens))  # 6
print(next(evens))  # StopIteration




#Faster way 
def get_multiples(count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num
