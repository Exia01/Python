class Aquatic:
    def __init__(self, name):
        self.name = name

    def swim(self):
        return f'{self.name} is swimming'

    def greet(self):
        return f'I am {self.name} of the sea!'

class Ambulatory:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f'{self.name} is walking'
    
    def greet(self):
        return f'I am {self.name} of the land!'
    

class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        super().__init__(name=name)

jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
Captain_cook = Penguin("Captain Cook")

print(jaws.swim())
print(lassie.walk())
Captain_cook.swim()
Captain_cook.walk()
print(Captain_cook.greet()) # uses greet from land

# we could do both is instance to test