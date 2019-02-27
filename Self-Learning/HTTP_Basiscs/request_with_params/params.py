import requests
url = "https://icanhazdadjoke.com/search"  # site for making requests

response = requests.get(
    url,
    headers={"Accept": "application/json"},  # The header requesting JSON
    params={"term": "cat", "limit": 1}  # request with the limit of one joke
)

data = response.json()
print(data["results"])


""" https://www.google.com/search?source=hp&ei=IOd1XP__F82GsQXXjJrIDg&q=american+marten&btnK=Google+Search&oq=american+marten&gs_l=psy-ab.3..0l10.4578.6601..6806...0.0..0.192.1384.13j2......0....1..gws-wiz.....0..0i10.61qoPANEaKQ """

# this is an example of a query search based off of a "?" query value
