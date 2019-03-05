from random import choice
#here we can change the methods for this class
class GrumpyDict(dict): #no init since we inherit from dictionary

	def __repr__(self):
		messages  = ["LEAVE ME ALONE!", "Not YOU AGAIN!", "NONE OF YOUR BUSINESS"]
		print(choice(messages))
		return super().__repr__() #dictionarys version of __repr__

	def __missing__(self, key):
		print(f"YOU WANT {key}?  WELL IT AINT HERE!")
		raise KeyError(key)

	def __setitem__(self, key, value):
		print("YOU WANT TO CHANGE THE DICTIONARY?")
		print("OK FINE...")
		super().__setitem__(key, value) #sets items

	def __contains__(self, item):
		print("NO IT AINT IN HERE!")

data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data, "\n")
data.get('city', None)
data['city'] = 'Tokyo'
# print(data)
print('city' in data)





























class GrumpyDict(dict):
	def __repr__(self):
		print("NONE OF YOUR BUSINESS")
		return super().__repr__()

	def __missing__(self, key):
		print(f"THAT THING YOU WANT ISN'T IN HERE")

	def __setitem__(self, key, value):
		print("Why do you always have to change things?")
		print(f"Ugh fine, setting {key} to {value}")
		super().__setitem__(key, value)