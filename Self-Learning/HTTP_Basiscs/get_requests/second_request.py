import requests
url = "http://www.google.com" # if we remove the http, we a removing the protocol. Won't work
# url = "http://www.google.com/adsf/sdss" #404 
response = requests.get(url) # get request

print(f"your request to {url} came back w/ status code {response.status_code}")

print(response.text)