items = [1, 2, 3, 4, 'socks', 'vortex', 'socks', [1, 2]]

x = items.index("socks")  # will print out the position
print(x)
y = items.index("socks", 5)  # looking from position 5, can also pass an end
print(y)
a = items.count('socks')
print(a)

# reverse
items.reverse()
print(items)


# copy
another_list = items.copy()
somelist = [x for x in another_list if not type(x) == str]

# reverse
somelist.reverse()
print(somelist)


# join is not a list method, it is a string method
names = ['Hello', 'World']
x = ' '.join(names)
print(x)


names = ['John', 'Timmy']
friends = ', '.join(names)
print(f'I am friends with {friends}')
