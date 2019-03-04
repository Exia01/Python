# A User class with both instance attributes and instance methods
class User:
    active_users = 0

    @classmethod  # These spread outs across the entire class not instances "User" is being passed
    def display_active_users(cls):  # class is passed as instance
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):  # clas since it class wide
        first, last, age = data_str.split(",")  # splits the string
        # cls here is the class itself; creates new user
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def login(self):
        if isinstance(self, Moderator):
            Moderator.total_mods +=1
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


# every Moderator gets all those methods
class Moderator(User):
    total_mods = 0

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)  # attributes from parent
        self.community = community

    @classmethod
    def display_active_mods(cls):  # class is passed as instance
        return f"There are currently {cls.total_mods} active mods"

    def remove_post(self, other_user):
        return f'{self.full_name()} removed a post from {other_user.full_name()} in the {self.community} community'



Jasmine = Moderator('Jasmine', 'O\'conner', 65, 'Piano')
Robert = User('Robert', 'Smith', 78)
print(Jasmine.login())
print(Robert.login())


print(User.display_active_users())
print(Moderator.display_active_mods())
# print(Jasmine.full_name())
# print(Jasmine.community)
# print(issubclass(Moderator, User))
print(Jasmine.remove_post(Robert))