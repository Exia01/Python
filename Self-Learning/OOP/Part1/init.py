# A User class with 3 attributes but no methods (aside from __init__)
class User:
                # init, equivalent of constructor
    def __init__(self, first, last, age, is_admin=False):  # self refers to the instance
        self.first = first
        self.last = last
        self.age = age
        self.is_admin = is_admin


user1 = User("Joe", "Smith", 68, True)
user2 = User("Blanca", "Lopez", 41)
print(user1.first, user1.last, user1.age, user1.is_admin)
print(user2.first, user2.last, user2.age, user2.is_admin)
