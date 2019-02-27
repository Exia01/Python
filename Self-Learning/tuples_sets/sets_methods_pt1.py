# add
s = set({1, 2, 3, 4, })
s.add(4)
print(s)
s.add(4)  # wont add another one but won't throw error
print(s)

cities = {"Los Angeles", "Kyoto", "Florence", "Santiago"}
cities.add("Tokyo")
print(cities)

#remove
s = set({1, 2, 3, 4,})
s.remove(3)
print(s)

cities.remove("Tokyo")
print(cities)  # if not found will throw KeyError
cities.discard("Tokyo") # will not throw error but wont remove
print(cities.discard("Kyoto"))

#Copy
cities_copy = cities.copy()
print(cities_copy)
print(cities_copy is cities)  # false

#set Math


# clear --> removes the entire content
cities.clear()
print(cities)