s = set({1, 2, 3, 4, 5, 7, 7})  # 1,2,3,4,5,7
# can't have duplicates
print(s)


# creating a new set
sample = set({1, 4, 5})
print(sample)

# Can also be used to create a set?
sample1 = {1, 4, 5}
print(4 in sample)

sample_2 = {1, 2, 35, 45, 'a', 'b', 23.4059}
print(sample_2)

for item in sample_2:
    print(item)

cities = ["Los Angeles", "Kyoto", "Florence", "Santiago", "Kyoto", "Boulder", "Los Angeles"]
# unique cities 
print(len(set(cities)))
print(cities)
print(set(cities))
set_cities = set(cities)
reverted_cities = list(set_cities)

print(set_cities)
print(reverted_cities)