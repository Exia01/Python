""" 
A parameter is a variable in a method definition
Argument is the actual value of the variable or "Parameter" that gets passed into the function
"""

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']
colors.append('violet')
print(colors)

# .append, print, .clear these are all built-in function

# defining a function


def say_hi():
    print('Hi!')


say_hi()


def sing_happy_birthday():
    print('Happy Birthday To You')
    print('Happy Birthday To You')
    print('Happy Birthday Dear You')
    print('Happy Birthday To You')


print(sing_happy_birthday())

# passing arguments


def sing_happy_birthday_2(name):
    print('Happy Birthday To You')
    print('Happy Birthday To You')
    print(f'Happy Birthday Dear {name}')
    print('Happy Birthday To You')


sing_happy_birthday_2("Timmy")

num = 50


def generate_evens(num):
    total = [i for i in range(0, num, 2)]
    return total


print(generate_evens(num))


def generate_evens2():
    return [x for x in range(1, 50) if x % 2 == 0]
