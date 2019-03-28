# importing modules
import requests
from csv import DictReader, DictWriter
from bs4 import BeautifulSoup
from pathlib import Path
# custom packages
from csv_writter import quotes_writer


data_folder = Path(
    r'C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\_Web_Scraping\projects\scraping_quotes\csv_files')
filename = "quotes.csv"

quotes_file = data_folder / filename

site = 'http://quotes.toscrape.com'
page = 1


with open(quotes_file, 'w', encoding='utf-8-sig') as csv_file:
    headers = ("quote", "author", "bio_link", "tags")
    csv_writer = DictWriter(csv_file, fieldnames=headers, lineterminator="\n")
    csv_writer.writeheader()
    while True:
        data = requests.get(site)
        soup = BeautifulSoup(data.text, "html.parser")
        if data:
            quotes = soup.find_all(class_="quote")
            try:
              next_page = soup.find("li", {"class": "next"}).find(
                "a", recursive=False)['href']
            except AttributeError:
                next_page = None
            else:
                next_page =  soup.find("li", {"class": "next"}).find(
                "a", recursive=False)['href']
            quotes_writer(quotes, csv_writer)
            if next_page is not None:
                site = f"http://quotes.toscrape.com{next_page}"
                page +=1
            else:
                break
