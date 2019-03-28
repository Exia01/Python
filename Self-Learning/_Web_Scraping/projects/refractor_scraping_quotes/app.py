# importing modules
import requests
from csv import DictReader, DictWriter
from bs4 import BeautifulSoup
from pathlib import Path
# custom packages
from csv_writter import quotes_writer
from time import sleep
from random import choice


data_folder = Path(
    r'C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\_Web_Scraping\projects\scraping_quotes\csv_files')
filename = "quotes.csv"


quotes_file = data_folder / filename
# making request
# all caps makes it a const --> constant
BASE_URL = 'http://quotes.toscrape.com'


def scrape_quotes():
    all_quotes = []
    url = '/page/1'
    while url:
        res = requests.get(f'{BASE_URL}{url}')
        # print(f'Now Scrapping {BASE_URL}{url}....')
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find("small", {"class": "author"}).get_text(),
                "bio-link": quote.find("a")["href"]
            })
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        # sleep(3)
    return all_quotes


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


quotes = scrape_quotes()
start_game(quotes)
