def exponent(num, power=2):
    return num ** power


# Order doesn't matter anymore, if we use key word arguments:
print(exponent(num=2, power=3))  # 8
print(exponent(power=3, num=2))  # 8

# Without keywords args, order still matters:
print(exponent(3, 4))  # 81
print(exponent(4, 3))  # 64


# Another sample,
def full_name(first, last):  # setting parameter
    return f'Your name is {first} {last}'


print(full_name(first='Jose', last="Gonzalez"))
# we can also change the order of arguments
print(full_name(last="Gonzalez", first='Jose'))


""" Non local Variable """


def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count
    return inner()
