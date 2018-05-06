# declare a class and give it name User
class User(object):
    # the __init__ method is called every time a new object is created
    def __init__(self, name, email):
        # set some instance variables. just like any variable we can call these anything
        self.name = name
        self.email = email
        self.logged = False
    # this is a method we created to help a user login

    def login(self):
        self.logged = True
        print(self.name + " is logged in.")
        return self


# now create an instance of the class
new_user = User("Anna", "anna@anna.com")
print(new_user.email)


# class user1(object):
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.logged = False


# user2 = User("Anna Propas", "anna@anna.com")
# print(user2.name)
# print(user2.logged)
# print(user2.email)


class bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print(self.price, self.miles, self.max_speed)

    def ride(self):
        self.miles += 10
        return self

    def reverse(self):
        self.miles -= 5
        return self


bike1 = bike(200, 25)
bike2 = bike(150, 50)
bike3 = bike(150, 50)

bike1.ride().ride().ride().reverse().displayInfo()
bike2.displayInfo()

class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    # def number_of_wheels(self):
    #     return self.number_of_wheels

    # def number_of_wheels(self, number):
    #     self.number_of_wheels = number
    #     return self


tesla_model_s = Vehicle(4, 'electric', 5, 250)
print(tesla_model_s.number_of_wheels)  # 4
tesla_model_s.number_of_wheels = 2  # setting number of wheels to 2
print(tesla_model_s.type_of_tank)  # 2
