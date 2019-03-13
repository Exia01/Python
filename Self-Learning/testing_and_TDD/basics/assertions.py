# Example1
def add_positive_numbers(x, y):
        # first assert, then expression, message is optional
    assert x > 0 and y > 0, "Both numbers must be positive! -> {}, {}".format(
        x, y)
    return x + y


# test cases
print(add_positive_numbers(1, 1))  # 2
add_positive_numbers(1, -1)  # AssertionError: Both numbers must be positive!


# Example 2
def eat_junk(food):
    assert food in [  # truth or false
        "pizza",
        "ice cream",
        "candy",
        "fried butter"
    ], "food must be a junk food!"
    return f"NOM NOM NOM I am eating {food}"

#test case
food = input("ENTER A FOOD PLEASE: ")
print(eat_junk(food))
