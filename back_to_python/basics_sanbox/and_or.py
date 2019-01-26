question = "What City do you live in? LA or San francisco?"
print(question)
city = input()
city.lower()
try:
    city == "san francisco" or city == "la":
        print("Cool! I have a cousin that lives there!")
except:
    print(f'That\'s cool! I\'ve never been to {city}.')