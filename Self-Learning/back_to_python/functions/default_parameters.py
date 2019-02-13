
def intruder_alert(first_name="Jose", is_primary_user=False):
    if first_name == "Jose" and is_primary_user:
        return "Welcome back Jose!"
    elif first_name == 'Jose':
        return "I thought you were the primary user???"
    return f'Hello {first_name}'


print(intruder_alert("Jose"))
print(intruder_alert("Jose", True))
print(intruder_alert("Jimmy"))


default_value = 2


def exponent(num, power=2):  # takes a num raised to a power
    return num ** power


print(exponent(2, 3))  # 8
print(exponent(3))  # 9
print(exponent(7))  # 49


# other functions can be passed as well
def add(a, b):  # add function
    return a+b


def subtract(a, b):
    return a - b


def math(a, b, fn=add):  # passing add function as a parameter
    return fn(a, b)


print(math(4, 5))  # results in add(4,5) which is 9

print(math(4, 5, subtract))  # results in subtract(4,5) which is -1

# Another example:


class Animal:
    def __init__(self, sound):
        self.sound = sound

    def speak(self):
        return self.sound

test = Animal(None)
pig = Animal("oink")
duck = Animal("quack")
cat = Animal("meow")
dog = Animal("woof")
chimera = Animal("?")
animals = [pig, duck, cat, dog, chimera, chimera]
def speak(klass=dog, lookup = animals):
    if klass not in lookup:
        return "?"
    return klass.speak()

print(speak(test))

def speak_2(animal='dog'):
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    return noises.get(animal, '?')