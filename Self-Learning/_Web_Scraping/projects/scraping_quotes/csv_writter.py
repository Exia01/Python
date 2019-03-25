
def quotes_writer(quotes, csv_writer):
    for quote in quotes:
            tags = quote.find("div", {"class": "tags"})
            quote_text = quote.find(class_="text").get_text()
            author = quote.find("small", {"class": "author"}).get_text()
            author_href = f'http://quotes.toscrape.com{quote.find_all("span")[1].find("a")["href"]}'
            categories = quote.find("meta")['content']
            if categories is "":
                categories = "No tags found"
            csv_writer.writerow({
                "quote": quote_text,
                "author": author,
                "bio_link": author_href,
                "tags": categories
            })

if __name__ == "__main__":
    quotes_writer(quote_block)  # prevents it from running at start
