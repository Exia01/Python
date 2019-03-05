class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age = age  # private class

    # could use a getter
    # def get_age(self):
    #     return self._age

    @property  # decorator, acts as a attribute Or setter
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age can't ne negative!")
    
    @property
    def full_name(self):
        return f'{self.first} {self.last}'


jane = Human("Jane","Goodall", 50)
print(jane.age)
jane.age = 20
print(jane.age)
print(jane.full_name)
