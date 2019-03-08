def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite #ties it in and wwe don't have to set it as a variable
def greet():
    print("My name is Colt.")


@be_polite #another example of wrapping it
def rage():
	print("I HATE YOU!")


greet()
rage()