# A User class with both a class attribute
class User:
	# this is part of the class as an attribute
	active_users = 0 #defined once for the whole class

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		self.logged_in = False

	def login(self):
		if self.logged_in == False:
			self.logged_in = True
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




# print(user1.likes("Ice Cream"))
# print(user2.likes("Chips"))

# print(user2.initials())
# print(user1.initials())

# print(user2.is_senior())
# print(user1.age)
# print(user1.birthday())
# print(user1.age)
# user1.say_hi()

user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(user1.login())
user2.login()
print(User.active_users)
print(user2.logout())
print(User.active_users)










