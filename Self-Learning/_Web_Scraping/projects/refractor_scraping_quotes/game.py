# importing modules
import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader
from pathlib import Path
# custom packages

data_folder = Path(
    r'C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\_Web_Scraping\projects\refractor_scraping_quotes\csv_files')
filename = "quotes.csv"

quotes_file = data_folder / filename
BASE_URL = 'http://quotes.toscrape.com'

def read_quotes(quotes_file):
    with open(quotes_file, 'r') as file:
        csv_reader = DictReader(file)
        return list(csv_reader)



def start_game(quotes):

    quote = choice(quotes)
    remaining_guesses = 4
    nope = "Nope!!! \n"
    print("Here's a quote: ")
    print(quote.get("text"))
    print(quote.get("author"))
    guess = " "
    while guess.lower() != quote.get("author").lower() and remaining_guesses > 0:
        guess = input(
            f'Who said this quote? Guesses remaining: {remaining_guesses} \n')
        if guess.lower() == quote.get('author').lower():
            print('You got it!!!')
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            print(nope)
            res = requests.get(f'{BASE_URL}{quote.get("bio-link")}')
            soup = BeautifulSoup(res.text, "html.parser")
            birth_date = soup.find(class_="author-born-date").get_text()
            birth_place = soup.find(class_="author-born-location").get_text()
            print(
                f'Here\'s a hint: the author was born on {birth_date} {birth_place}')
        elif remaining_guesses == 2:
            quote.get('author')[0]
            print(
                f"Here's a hint: The author's first name starts with {quote.get('author')[0]}")
            quote.get('author').split()[1][0]
        elif remaining_guesses == 1:
            last_initial = quote.get('author').split()[1][0]
            quote.get('author')[0]
            print(
                f"Here's a hint: The author's first last name starts with {last_initial}")
        else:
            print(
                f"Sorry, you ran out of guesses. The answer was {quote.get('author')}")

    print("After While Loop")
    again = " "
    options = ('y', 'yes', 'n', 'no', 'quit', 'q')
    while again.lower() not in options:
        again = input("Would you like to play again? (y/n)? ")
    if again.lower() in ('y', 'yes'):
        print("Great! let's play again!")
        return start_game(quotes)
    else:
        print("Cool! See ya later!")


quotes = read_quotes(filename)

start_game(quotes)
