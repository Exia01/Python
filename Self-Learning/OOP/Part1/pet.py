# Another class with a class attribute, used for validation purposes
class Pet:
	allowed = ['cat', 'dog', 'fish', 'rat'] #could move into init but if we want to reuse leave here

	def __init__(self, name, species):
		if species.lower() not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet!")
		self.name = name
		self.species = species

	def set_species(self,species):
		if species not in Pet.allowed: #could do self but this is more explicit
			raise ValueError(f"You can't have a {species} pet!")
		self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")
fiffy = Pet("Wyatt", "dog")
Pet.allowed.append('pig')
fiffy.set_species('pig')
print(fiffy.species)

#gives the unique id that python assigns 
print(id(cat.allowed))
print(id(fiffy.allowed)) #both are the same, all point and refer to the same class attribute

#could create an instace attribute and overwrite it
cat.allowed = ['Hello']
print(cat.allowed)
