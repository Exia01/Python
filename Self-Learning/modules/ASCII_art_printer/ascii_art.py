from pyfiglet import figlet_format #specific format
from termcolor import colored


def print_art(msg, color):
    valid_colors = ("red", "green", "yellow", "blue",
                    "magenta", "cyan", "white")

    if color not in valid_colors:
        color = "magenta"
    if not msg:
        msg = "No color passed"
    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)


print("What would you like to print? ")
msg = input()
print("What color? ")
color = input()
print_art(msg, color)
