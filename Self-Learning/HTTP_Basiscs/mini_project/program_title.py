from pyfiglet import figlet_format  # specific format
from termcolor import colored
from random import choice as pick

msg = " Dad Joke 8000! \n"


def program_greeter(msg=msg):
    'Prints a formatted greeter when starting program'
    colors = ("red", "green", "yellow", "blue",
              "magenta", "cyan", "white")
    color = pick(colors)
    ascii_art = figlet_format(msg)  # formats the message
    colored_ascii = colored(ascii_art, color)
    print(colored_ascii)


if __name__ == "__main__":
    program_greeter()  # prevents it from running at start
