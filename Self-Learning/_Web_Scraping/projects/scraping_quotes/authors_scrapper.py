import requests
from csv import DictReader, DictWriter
from bs4 import BeautifulSoup
from pathlib import Path
# custom packages

data_folder = Path(
    r'C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\_Web_Scraping\projects\scraping_quotes\csv_files')

authors_bio = data_folder / "authors_bio.csv"
quotes_file = data_folder / "quotes.csv"


site = ""
authors_dictionary = {}
authors_list = []


with open(quotes_file, 'r', encoding='utf-8-sig') as f:
    csv_reader = DictReader(f)
    authors_list = list(csv_reader)
    for quote in authors_list:
        author = f'{quote.get("author")}'
        try:
            authors_dictionary[author]
        except KeyError:
            # authors_dictionary[author] = (quote.get("bio_link"), 0)
            authors_dictionary[author] = 0


with open(authors_bio, 'w', encoding='utf-8-sig') as csv_file:
    # headers = ("name", "dob_location", "trivia_info")
    # csv_writer = DictWriter(csv_file, fieldnames=headers, lineterminator="\n")
    # csv_writer.writeheader()
    for author in authors_list:
        author_name = author.get("author")
        if authors_dictionary.get(author_name) == 0: #true if 1
            site = author.get("bio_link")
            
            data = requests.get(site)
            soup = BeautifulSoup(data.text, "html.parser")
            bod = soup.find("div", {"class": "author-details"}).find_next().find_next().get_text().split(":")[1][1::]
            trivia = soup.find("div", {"class":"author-description"}).get_text().strip("\n")
            print(trivia)
            break
            # csv_writer.writerow({
                # "name": author_name,
                # "dob_location"

            # })


# print(authors_dictionary)

""" 
  for quote in csv_reader:
        author = f'{quote.get("author")}'
        try:
            authors_dictionary[author]
        except KeyError:
            # authors_dictionary[author] = (quote.get("bio_link"), 0)
            authors_dictionary[author] = 0
    print(authors_dictionary) """