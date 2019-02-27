#This demonstrate the different the order of arguments
def display_info(a, b, *args, Teacher="John", **kwargs):
    print(type(args))  # tuple
    return [a, b, args, Teacher, kwargs]


print(display_info(1, 2, 3, last_name="Stein", job="Instructor"))
print(display_info(1, 2, [232, 289], 8, 90,
                   last_name="Stein", job="Instructor"))

# a - 1
# b - 2
# args (3)
# Teacher - "John"
# kwargs - {'last_name': "Steele", "job": "Instructor"}

[1, 2, (3,), 'John', {'last_name': 'Stein', 'job': 'Instructor'}]
