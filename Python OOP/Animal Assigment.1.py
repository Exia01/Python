class Animal:
    def __init__(self, name):
        print("This is good bruhhh1")
        self.health = 250
        self.name = name
        self.stealth = 1

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display(self):
        print("Current health of", self.name, "is", self.health)
        return self


spacepirate = Animal("Tropper Pirate")

spacepirate.walk().walk().walk().run().run()
spacepirate.display()


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("This fucking thing too", 2)
        self.health = 150
        self.name = name

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def pet(self):
        self.health += 5
        return self

    def display(self):
        print("Health of", self.name, "is", self.health)
        return self


terrier = Dog("Sparky")
terrier.walk().walk().walk().run().run().pet()
terrier.display()


class Dragon(Animal):
    def __init__(self, name):
        super().__init__(name)
        print("This fucking thing too", 2)
        self.health = 170
        self.name = name

    def fly(self):
        self.health -= 10
        return self

    def Eatahobbit(self):
        self.health += 5
        return self

    def display(self):
        print("Health of", self.name, "is",
              self.health, "Caution, here be dragons")
        print("you shall not pass")
        return self


Smaug = Dragon("Smaug")
Smaug.fly().fly().Eatahobbit().Eatahobbit()
Smaug.display()
