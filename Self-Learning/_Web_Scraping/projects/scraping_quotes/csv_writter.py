from pathlib import Path
from csv import DictReader, DictWriter


data_folder = Path(
    r'C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\_Web_Scraping\projects\scraping_quotes')
filename = "quotes.csv"
quotes_file = data_folder / filename

def quotes_writer(quote_block):
     for quote in quotes:
        tags = quote.find("div", {"class": "tags"})
        quote_text = quote.find(class_="text").get_text()
        author = quote.find("small", {"class": "author"}).get_text()
        author_href = f'http://quotes.toscrape.com{quote.find_all("span")[1].find("a")["href"]}'
        categories = quote.find("meta")['content']
        csv_writer.writerow({
            "quote": quote_text,
            "author": author,
            "bio_link": author_href,
            "tags":categories
        })


if __name__ == "__main__":
   quotes_writer(quote_block)  # prevents it from running at start
