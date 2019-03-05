from copy import copy
##this use the dunder method 
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		
	def __repr__(self): #repr or representation method
		return f"Human named {self.first} {self.last} aged {self.age}"

	def __len__(self): #length of a human? how about length of time
		return self.age

	def __add__(self, other): # self, meaning instance and other other human 
		# When you add two humans together...you get a newborn baby Human!
		if isinstance(other, Human):
			return Human(first='Newborn', last=self.last, age=0)
		return "You can't add that!" # or raise a type error

	def __mul__(self, other):
		# When you multiply a Human by an int, you get clones of that Human!
		if isinstance(other, int):
			return [copy(self) for i in range(other)] # will make a copy --> space in memory
		return "CANT MULTIPLY!" # or raise a type error
	


j = Human("Jenny", "Larsen", 47)
k = Human("Kevin", "Jones", 49)
# print(j)
# print(len(j))
# triplets = j * 3

# kevin and Jenny have triplets!
print(j+k)
triplets = (k + j) * 3
triplets[1].first = 'Jessica'
print(triplets)
