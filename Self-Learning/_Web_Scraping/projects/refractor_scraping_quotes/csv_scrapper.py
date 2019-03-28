# importing modules
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice
from csv_writter import write_quotes


# making request
# all caps makes it a const --> constant
BASE_URL = 'http://quotes.toscrape.com'


def scrape_quotes():
    all_quotes = []
    url = '/page/1'
    while url:
        res = requests.get(f'{BASE_URL}{url}')
        res.encoding = 'utf-8'
        print(f'Now Scrapping {BASE_URL}{url}....')
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
        sleep(3)
    return all_quotes


quotes = scrape_quotes()
# Write quotes to csv file
write_quotes(quotes)