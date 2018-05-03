# # num1 = [1, 2, 3, 4]
# #
# #
# # def newnum(num1):
# #     dic1 = {}
# #     dic1['min'] = num1[0]
# #     dic1['max'] = num1[0]
# #     dic1['sum'] = 0
# #     for i in (num1):
# #         if dic1['min'] > i:
# #             dic1['min'] = i
# #         if dic1['max'] < i:
# #             dic1['max'] = i
# #         dic1['sum'] += i
# #
# #     dic1['average'] = dic1['sum'] / (len(num1))
# #
# #     print(dic1)
# #
# #
# # newnum(num1)
#
# # Basic
# for count in range(0, 151, 10):
#     print(count)
#
# #multiples of 5
# for count in range(5, 1000000, 5):
#     print(count)
#
#  #Counting the Dojo way
# for i in range(1, 100):
#     if i % 10 == 0:
#         print('Dojo', i)
#     elif i % 5 == 0:
#         print('Coding', i)
#     else:
#         print(i)
#
#  Whoa that sucker is huge
# total = 0
#
# for i in range(0, 500000, 1):
#     if i % 2 != 0:
#         total += i
# print(total)
#
#  Countdown by Fours
# for i in range(2018, -2, -4):
#     print(i)
#
#  Flexible Countdown
# for i in range(12, 1, -3):
#     print(i)


# Starts here
def a():
    return 5


print(a())  # will print 5 because of inside definition


def a():
    return 5


print(a() + a())  # will return 10


def a():
    return 5
    return 10


print(a())  # will return 5


def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10


print(a)


# """will print 100 and return 5"""

def a(b, c):
    if b < c:
        return 7
    else:
        return 14
    return 3


print(a(2, 3))
print(a(5, 3))
print(a(2, 3) + a(5, 3))


# """this will add both values"""


def a(b, c):
    return b + c
    return 10


print(a(3, 5))

b = 500
print(b)


# """will print 500"""


def a():
    b = 300
    print(b)
    print(b)
    a()
    print(b)


# """this will print in a loop"""

b = 500
print(b)  # this stores a variable outside will print 500


def a():  # this creates the variable b inside.
    b = 300
    print(b)
    return b


a()  # calls the function, will print 300'''
print(b)  # will print 500
a()  # ill print 300
print(b)
# will print 500

b = 500
print(b)


def a():
    b = 300
    print(b)
    return b


a()
print(b)
a()
print(b)
