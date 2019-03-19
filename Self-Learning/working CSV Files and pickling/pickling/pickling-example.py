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


blue = Cat("Blue", "Scottish Fold", "String")
red = Cat("Red", "Scottish Fold", "String")

# To pickle an object:
with open(file, "wb") as f: # we need to convert it into a bytestream so use b
    pickle.dump((red, blue), f) # takes in the object/ or multiple ones and then the file

# # To unpickle something:
# with open(file, "rb") as pickle_file: #reading from binary so rb is needed.
# 	zombie_blue = pickle.load(pickle_file)
# 	print(zombie_blue)
# 	print(zombie_blue.play())
