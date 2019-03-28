from pyfiglet import figlet_format  # specific format
from termcolor import colored
from random import choice as pick
from csv import reader, DictReader
from pathlib import Path
from random import choice

msg = "Trivia!\n"
def program_greeter(msg=msg):
    'Prints a formatted greeter when starting program'
    colors = ("red", "green", "yellow", "blue",
              "magenta", "cyan", "white")
    color = pick(colors)
    ascii_art = figlet_format(msg)  # formats the message
    colored_ascii = colored(ascii_art, color)
    print(colored_ascii)

program_greeter()
data_folder = Path(
    r"C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\_Web_Scraping\projects\scraping_quotes\csv_files")

quotes_file = data_folder / "quotes.csv"
authors_file = data_folder / "authors_bio.csv"


def trivia_game(authors_file=authors_file, quotes_file=quotes_file):
    print("Guest a quote from an author")
    print("You have 4 tries!")
    # name_term = input()
    with open(quotes_file, 'r', encoding='utf-8-sig') as quote_f, open(authors_file, 'r', encoding='utf-8-sig') as author_file:
        quote_csv_reader = list(DictReader(quote_f))
        author_csv_reader = list(DictReader(author_file))
        print(author_csv_reader)
    while True:
        tries = 4
        selection_1 = choice(quote_csv_reader)
        print(selection_1)
        temp_name = selection_1.get("author")
        print("Who said this: \n")
        print(selection_1.get("quote"),"\n")
        name_term = input("Full Name, Take a guess: ").lower()
        # again_response = input().lower()
        comparison = name_term == temp_name.lower()
        state = print("You got it! it's", temp_name)
        if comparison:# if True
            state
            break
        elif not comparison:
            tries -= 1
            print("Nope!\n", tries, "left")
            print("Here's a hint, firt name initial is", temp_name[0])
            name_term = input("Full Name, Take a guess: ").lower()
        if comparison:
            state
            break
        elif not comparison:
            tries -= 1
            x = temp_name.split()[1][0]
            print("Nope!\n", tries, "left")
            print("Here's a hint, last name initial is", x)
            name_term = input("Full Name, Take a guess: ").lower()
        if comparison:
            state
            break
        
        break


trivia_game()