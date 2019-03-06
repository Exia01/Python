# Inheritance Example Using Super()
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy): #instance specific attributes
		super().__init__(name, species="Cat")  # Call init on parent class
		#refers to parent class --> cat and passes self automatically
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")



blue = Cat("Blue","Scottish Fold", "String")
print(blue.species)
print(blue.breed)
print(blue.toy) 
blue.play()
print(blue)
print(blue.make_sound('Meow'))


# "MODEL" FOR ANIMAL AND CAT
# Animal
# 	species
# 	name

# Cat
# 	species
# 	name
# 	breed
# 	favorite_toy