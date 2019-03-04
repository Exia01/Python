# Chicken Coop Exercise
# Suppose we have a big ol chicken coop in our backyard full of very productive hens. We're going to model our chickens with python! We
# want to keep track of how many eggs each individual Chicken lays, and at the same time we want to track the total number of eggs all
# hens have laid.
# Create a Chicken class. Each Chicken has a species and a name, aswell as an integer attribute called eggs. eggs should always
# start out at 0.
# Each Chicken should also have an instance method called lay_egg()  which should increment and then return that particular Chicken's
# eggs attribute. lay_egg() should also increment a class variable called total_eggs


class Bird:
    total_eggs = 0

    def __init__(self, name, can_fly):
        self.name = name
        self.can_fly = can_fly
        self.eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Bird.total_eggs += 1
        return self.eggs


class Chicken(Bird):
    def __init__(self, name, species, can_fly=False):
        Bird.__init__(self, name, can_fly) # could also user super. 
        self.species = species

    def clucks(self):
        return "cluck cluck cluck"


# Test Cases
c1 = Chicken("Alice", "Partridge Silkie", True)
c2 = Chicken(name="Amelia", species="Speckled Sussex", can_fly=False)
print(Chicken.total_eggs)  # 0
print(c1.lay_egg())  # 1
print(Chicken.total_eggs)  # 1
print(c2.lay_egg())  # 1
print(c2.lay_egg())  # 2
print(Chicken.total_eggs)  # 3
print(c1.can_fly)
print(c1.clucks())
