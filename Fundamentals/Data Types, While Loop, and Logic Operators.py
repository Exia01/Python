name = "keyword operator from-rainbow" >= "Joe Blue"  # storing a string
age = 35  # storing an int
weight = 160.57  # storing a float
dead = False  #  storing a boolean
ninjas = ['Rozen', 'KB', 'Oliver']  # storing lists
new_person = {"name": "John", "age": 35, "weight": 160.2,
              "dead": False}  # storing dictionaries
# list
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []
print(ninjas[0])  # prints Rozen
print(ninjas[1])  # prints KB
print(ninjas[2])  # prints Oliver
print(len(ninjas))  # prints the length of the ninjas list
ninjas.append("Michael")  # adds Michael to the end of ninjas
ninjas.pop()  # pops the last value in the list
ninjas.pop(1)  # pops index 1 off the list
ninjas[2] = 'John'  # updates index 2's value to John
# if statements
if age >= 18:
    print('Your age is above 18.')
elif age == 17:
    print('You are seventeen.')
else:
    print('You are so young!')
# for loops
for count in range(0, 5):
    print("looping - ", count)
# looping through an array
for element in ninjas:
    print(element)
# define a function that returns the sum of two numbers


def sum(a, b):
    print("a:", a, "b:", b)  # prints the values of a and b
    return a + b  # returns the sum of a+b


print(sum(3, 5))
print(sum(2, 4) + sum(1, 5))
# define a function that says hello to the name provided
# this starts a new block


def say_hello(name=""):
    # these lines are indented and therefore part of the function
    if name:
        print('Hello, ' + name + ', from inside the function')
    else:
        print('No name')


# now we're unindented and have ended the previous block
print('Outside of the function')
