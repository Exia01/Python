from csv import DictReader, DictWriter
from pathlib import Path


def write_quotes(quotes):
    data_folder = Path(
        r'C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\_Web_Scraping\projects\refractor_scraping_quotes\csv_files')
    filename = "quotes.csv"

    quotes_file = data_folder / filename
    
    with open(quotes_file, "w", encoding='utf-8') as file:
        headers = ("text", "author", "bio-link")
        csv_writer = DictWriter(
            file, fieldnames=headers, lineterminator="\n")
        csv_writer.writeheader()
        for quote in quotes:
            print(quote)
            csv_writer.writerow(quote)  # already a dictionary


if __name__ == "__main__":
    write_quotes(quotes)  # prevents it from running at start
