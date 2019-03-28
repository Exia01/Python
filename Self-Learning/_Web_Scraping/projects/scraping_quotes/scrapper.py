# importing modules
import requests
from csv import DictReader, DictWriter
from bs4 import BeautifulSoup
from pathlib import Path
# custom packages
from csv_writter import quotes_writer
from time import sleep


data_folder = Path(
    r'C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\_Web_Scraping\projects\scraping_quotes\csv_files')
filename = "quotes.csv"

all_quotes = []
quotes_file = data_folder / filename
# making request
base_url = 'http://quotes.toscrape.com'
url = '/page/1'

while url:
    res = requests.get(f'{base_url}{url}')
    print(f'Now Scrapping {base_url}{url}....')
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
print(all_quotes)


# page = 1


# with open(quotes_file, 'w', encoding='utf-8-sig') as csv_file:
#     headers = ("quote", "author", "bio_link", "tags")
#     csv_writer = DictWriter(csv_file, fieldnames=headers, lineterminator="\n")
#     csv_writer.writeheader()
#     while True:
#         data = requests.get(site)
#         soup = BeautifulSoup(data.text, "html.parser")
#         if data:
#             quotes = soup.find_all(class_="quote")
#             try:
#               next_page = soup.find("li", {"class": "next"}).find(
#                 "a", recursive=False)['href']
#             except AttributeError:
#                 next_page = None
#             else:
#                 next_page =  soup.find("li", {"class": "next"}).find(
#                 "a", recursive=False)['href']
#             quotes_writer(quotes, csv_writer)
#             if next_page is not None:
#                 site = f"http://quotes.toscrape.com{next_page}"
#                 page +=1
#             else:
#                 break
