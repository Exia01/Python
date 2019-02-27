# Example of requests
import requests
res = requests.get('https://news.ycombinator.com/')
print(res)
print(res.ok)
print(res.headers)
print(res.text)