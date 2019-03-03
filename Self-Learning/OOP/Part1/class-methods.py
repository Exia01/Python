# A User class with both instance attributes and instance methods
class User:
	active_users = 0

	@classmethod # These spread outs across the entire class not instances "User" is being passed
	def display_active_users(cls): #class is passed as instance
		return f"There are currently {cls.active_users} active users"

	@classmethod
	def from_string(cls, data_str): #clas since it class wide
		first,last,age = data_str.split(",") #splits the string
		return cls(first, last, int(age)) #cls here is the class itself; creates new user

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

	def login(self):
		User.active_users += 1
		return f"{self.first} has logged in"
	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"



user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(user1.login())
print(user2.login())
print(User.display_active_users()) #using class method
# user1 = User("Joe", "Smith", 68)
# user2 = User("Blanca", "Lopez", 41)
# print(User.display_active_users())

tom = User.from_string("Tom,Jones,89")
print(tom.first)
print(tom.full_name())
print(tom.birthday())












