# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
  # Constructor --> defines the amount of arguments this == self
  def __init__(self, name, email, age=None):
    self.name = name
    self.email = email
    self.age = age

  #method takes in self( which is this) and variables
  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'
  
  def has_birthday(self):
    self.age += 1

# Customer class --> extends user
class Customer(User):
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0
    # initializes the balance at 0 by default

  def set_balance(self, balance):
    self.balance = balance

  def greeting(self):
    return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}'
    #this could also be done with super, or inheritance and added onto it. 

# Init / initialize a user object
Jose = User('Jose Gonzalez', 'jose@gmail.com', 37)
janet = User('Janet Williams', 'janet@gmail.com', 27)

# Edit property -> directly access properties
Jose.age = 38

janet.has_birthday() #incremented age by one

# Call method
print(janet.greeting())

# Init customer
john = Customer('John Doe', 'john@gmail.com', 40)

john.set_balance(500)

print(john.greeting())