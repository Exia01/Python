# EXAMPLE OF A SCOPING PROBLEM:
total = 0


def increment():
    total += 1  # local scope we have not instanciating before using 
    return total


print(increment())  # Error!
# "I can't find a variable named total in this function"


""" Using Global scope --> NOT RECOMMENDED """
total = 0


def increment_2():
    global total  # use the global variable total
    total += 1
    return total


print(increment_2())  # 1
print(increment_2())  # 2
print(increment_2())  # 3
