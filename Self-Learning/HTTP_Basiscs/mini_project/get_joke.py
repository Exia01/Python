import requests
url = "https://icanhazdadjoke.com/search"  # site for making requests


def request_jokes(search_term, joke_count):
    response = requests.get(
        url,
        headers={"Accept": "application/json"},  # The header requesting JSON
        # request with the limit of one joke
        params={"term": search_term, "limit": joke_count}
    )
    data = response.json()
    return data


