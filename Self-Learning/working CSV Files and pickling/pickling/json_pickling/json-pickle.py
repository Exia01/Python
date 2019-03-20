import jsonpickle  # pip install first
from csv import reader, DictReader
from pathlib import Path

data_folder = Path(
    r"C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\working CSV Files and pickling\pickling\json_pickling")
filename = "cat.json"
# generates an instance each time it is used
json_pickle_file = data_folder / filename


class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def meow(self):
        print("Meow!")


# c = Cat("Charles", "Tabby")

# # To JSONPICKLE 'c' the cat:
# with open(json_pickle_file, "w") as file:
# 	frozen = jsonpickle.encode(c)
# 	file.write(frozen)


# To bring back 'c' the cat using JSONPICKLE
with open(json_pickle_file, "r") as file:
    contents = file.read()
    unfrozen = jsonpickle.decode(contents)
    print(unfrozen)  # we have a cat object and we can then call the methods
    print(unfrozen.meow())
