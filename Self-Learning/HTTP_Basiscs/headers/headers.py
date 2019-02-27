import requests
url = "https://icanhazdadjoke.com/" #https is for secure

response = requests.get(url) # Without the headers we receive back the whole site.
response = requests.get(url, headers={"Accept": "application/json"})
#accept is the format of what we can receive back; this case is json

data = response.json() #storing for manipulation and changing to json
print(data) # prints the dictionary
print(data.get("joke", None))
print(f"status: {data['status']}")


""" 
{"id":"ozsPmORZvzd","joke":"A bartender broke up with her boyfriend, but he kept asking her for another shot.","status":200}

 {'id': 'Z8UDIRuXLmb', 'joke': 'Who did the wizard marry? His ghoul-friend', 'status': 200} looks similar but the type is different
"""