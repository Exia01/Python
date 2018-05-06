# file vehicles.py
class Vehicle:
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles
        return self

    def reverse(self, miles):
        self.mileage -= miles
        return self

        # file vehicles.py


class Vehicle:
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles
        return self

    def reverse(self, miles):
        self.mileage -= miles
        return self


class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"


class Car(Vehicle):
    def set_wheels(self):
        self.wheels = 4
        return self


class Airplane(Vehicle):
    def fly(self, miles):
        self.mileage += miles
        return self


v = Vehicle(4, 8, "dodge", "minivan")
print(v.make)
b = Bike(2, 1, "Schwinn", "Paramount")
print(b.vehicle_type())
c = Car(8, 5, "Toyota", "Matrix")
c.set_wheels()
print(c.wheels)
a = Airplane(22, 853, "Airbus", "A380")
a.fly(580)
print(a.mileage)


class Parent:
  # parent methods and attributes here


class Child(Parent):  # inherits from Parent class so we define Parent as the first parameter
  # parent methods and attributes are implicitly inherited
  # child methods and attributes


def varargs(arg1, *args):
    print("Got " + arg1 + " and " + ", ".join(args))


varargs("one")  # output: "Got one and "
varargs("one", "two")  # output: "Got one and two"
varargs("one", "two", "three")  # output: "Got one and two, three"


class Wizard(Human):
    def __init__(self):
        super().__init__()  # use super to call the Human __init__() method
        # every wizard starts off with 10 intelligence, overwriting the 3 from Human
        self.intelligence = 10

    def heal(self):
        self.health += 10  # all wizards also get a heal() method


class Ninja(Human):
    def __init__(self):
        super().__init__()  # use super to call the Human __init__() method
        # every Ninja starts off with 10 stealth, overwriting the stealth of 1 from Human
        self.stealth = 10

    def steal(self):
        self.stealth += 5  # all ninjas also get a steal() method


class Samurai(Human):
    def __init__(self):
        super().__init__()  # use super to call the Human __init__() method
        # every Samurai starts off with 10 strength, overwriting the 2 from Human
        self.strength = 10

    def sacrifice(self):
        self.health -= 5  # all samurais also get a sacrifice() method
