# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
# userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30, "arr":[12, 4, 60, 10]}'
articles = [{
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
},
    {
    "userId": 2,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
},
    {
    "userId": 3,
    "id": 3,
    "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
    "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
}, ],

# print(userJSON)
# Parse to dict
# user = json.loads(userJSON) # for the first example
# json.loads is the equivalent of json.parse

# for article in articles:
#     print(article)

# articles = json.dumps(articles)

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

# carJSON = json.dumps(car)

# print(carJSON)
