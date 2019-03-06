# Method Resolution Order(MRO)
# is the order in which Python will look for methods on instances of that class


class A:
    def do_something(self):
        print("Method Defined In: A")


class B(A):
    def do_something(self):
        print("Method Defined In: B")


class C(A):
    def do_something(self):
        print("Method Defined In: C")


class D(B, C):
    pass
    def do_something(self):
        print("Method Defined In: D")

# obj = D()
# obj.do_something()
print(D.__mro__)
print(D.mro())
print(help(D))