def display_names(first, second):
    print(f"{first} says hello to {second}")


names = {"first": "John", "second": "Rusty"}

# display_names(names)  # nope..
display_names(**names)  # yup!


def add_and_multiply_numbers(a, b, c, **kwargs):
    print(a + b * c) 
    print("OTHER STUFF....")
    print(kwargs)


data = dict(a=1, b=2, c=3, d=55, name="Tony")
# d and name will be pass to kwargs

add_and_multiply_numbers(**data, cat='blue')  # 7
