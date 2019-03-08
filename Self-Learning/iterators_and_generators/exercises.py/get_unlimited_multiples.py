# get_multiples
# Write a function called get_multiples, which accepts a number and a count, and returns a generator that yields the rest count multiples of
# the number.
# The default number should be 1, and the default count should be 10.


def get_unlimited_multiples(number=None):
    if not number:
        number = 1
    next_num = number
    while True:
        yield next_num
        next_num += number

sevens = get_unlimited_multiples(7)
x = [next(sevens) for i in range(15)]
print(x)

ones = get_unlimited_multiples()
sample = [next(ones) for i in range(20)]
print(sample)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]