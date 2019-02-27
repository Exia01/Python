names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]
# could be simple
print(min(names))
print(max(names))

# finds the minimum length of a name in names
sample = min(len(name) for name in names)  # 3 based on the list
print(sample)

# what if we want to find the longest name itself??
sample2 = max(names, key=lambda n: len(n))  # Ollivander
print(sample2)



songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

# Finds the song with the lowerest playcount
# {"title": "happy birthday", "playcount": 1}
min(songs, key=lambda s: s['playcount']) 

# Finds the title of the most played song
max(songs, key=lambda s: s['playcount'])['title']  # YMCA


# some other examples
print(max('awesome'))  # w
print(min('awesome'))  # a

bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

print(max(bakery_stock))


# sort the numbers that are odd in list
custom = [1, 2, 3, 54, 523, 6498, 239048209, [39428049, 39283, 0]]
test = list(filter(lambda x: type(x) == int, custom))
print(sorted(test))


results = min(list(filter(lambda x: type(x) == int, custom)))
# take the list of numbers not the embedded list and return the minimum number
print(results)


custom = [1, 2, 3, 54, 523, 6498, 239048209, [39428049, 39283, 0]]
first = list(filter(lambda x: type(x) == int, custom))
other = custom[:-1:]
# print(other)
first.extend(custom[-1])
print(sorted(first))
