import pickle
from csv import reader, DictReader
from pathlib import Path

data_folder = Path(
    r"C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\working CSV Files and pickling\pickling")
filename = "pets.pickle"
file = data_folder / filename  # generates an instance each time it is used


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        print(f"this animal says {sound}")


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")  # Call init on parent class
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


with open(file, "rb") as pickle_file:  # reading from binary so rb is needed.
    zombie_red, zombie_blue = pickle.load(pickle_file) # or assign it and separate it
    print(zombie_red)
    print(zombie_red.play())
    
    print(zombie_blue)
    print(zombie_blue.play())
