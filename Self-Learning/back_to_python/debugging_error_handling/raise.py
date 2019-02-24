def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
	#better to separate errors to better understand problems
    if type(color) is not str:
        raise TypeError("color must be instance of str") 
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    if color not in colors:
        raise ValueError("color is invalid")  # can also leave blank
    print(f"Printed {text} in {color}")

#Test cases
colorize("Hello", "blue")
# colorize([], 'cyan')
# colorize(34, "red")
