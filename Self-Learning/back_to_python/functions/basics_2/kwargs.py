def increment(number=None, by=None):  # optional parameters should come after the required
    return number + by


print(increment(1, 2))  # 3 we can also use a args

#substituting *args for numbers
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
print(multiply(1, 2, 3, 4, 5))  # this will print out tuples..can't be modified

# using **kwargs as **user
def save_user(**user):
    print(user["id"])

print(save_user(id=1, name="Jose", age=22))


list_sample1 = [1, 2, 3, 4, 5, 6]
list_sample2 = [6, 7, 8, 9, 10]
add_command = "add"
remove_command = "remove"
a, b, c, d = 100, 500, 1000, 5000

beginning  = "beginning"
end  = "end"

def list_manipulation(**kwargs):
    # print(kwargs.items())
    for key, value in kwargs.items():
        # print(key, value)
        # print("%s = %s" % (key, value))
    # print(kwargs)

print(list_manipulation(list_sample1=list_sample1,add_command=add_command, remove_command=remove_command))