# a special operator, gathers remaining arguments as a tuples
def ensure_correct_info(*args): # can be called whatever but this is standard
    if "Jose" in args and "Gonzalez" in args:
        return "Welcome back Jose!"
    return "Note sure who you are"


print(ensure_correct_info("hello", False, 78))  # Not sure who you are...

print(ensure_correct_info(1, True, "Gonzalez", "Jose"))

#Another example 
def sum_all_nums(*args):
	print(args) # we just need the star at the start --> prints tuple
	total = sum(args)
	return total


print(sum_all_nums(5, 9, 5, 5))
print(sum_all_nums(5, 5, 5))

#Another example
def feed_me(*stuff):
	for thing in stuff:
		print(f"YUMMY I EAT {thing}")
feed_me("apple", "tire", "shoe", "salmon")


#One last one 
def contains_purple(*args):
    for item in args:
        if item == "purple":
            return True
    return False
    
# or one liner
def contains_purple_2(*args):
    if "purple" in args: return True
    return False

print(contains_purple("a", 99, "Blah blah PURPLE", 1, 'purple'))