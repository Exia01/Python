# https://www.rithmschool.com/blog
# importing dependencies
import requests
from csv import DictReader, DictWriter
from bs4 import BeautifulSoup
from pathlib import Path


data_folder = Path(
    r'C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\_Web_Scraping\first_scrapper_program')
filename = "articles.csv"
blog_file = data_folder / filename


# Requesting for data
response = requests.get("https://www.rithmschool.com/blog")
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")
with open(blog_file, "w") as csv_file:
    headers=("title", "link", "date")
    csv_writer = DictWriter(csv_file, fieldnames=headers,lineterminator="\n")
    csv_writer.writeheader()
    # print(articles)
    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag['href']
        date = article.find("time")["datetime"]
        csv_writer.writerow({
			"title":title,
			"link": url,
			"date": date
        })
        




