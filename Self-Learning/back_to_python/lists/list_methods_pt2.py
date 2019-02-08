
items = [1, 2, 3, 4, 'socks', 'vortex', 'socks', [1, 2]]

# Remove
# items.pop()  ### if left empty, wil remove last value by default
# items.pop(1)
last_item = items.pop()
print(last_item)

first_item = items.pop(0)
print(first_item)
print(items)


# remove --> removes first found "x" regardless of index, if not found throws value error
items.remove('socks')
print(items)

# items.clear()  #clears out the whole list
