# what is a tuple? too-pul or tuple  -- ordered collection or grouping of items that can't be changed "immutable"

numbers = (1, 2, 3, 4)

print(3 in numbers)

# numbers[0] = 2 # will produce an error

alphabet = ('a', 'b', 'c', 'd')
print(type(alphabet))

months = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')
# sincce this would not changed
print(months[11])
first_tuple = (1, 2, 3, 3, 5, 6)  # duplicate data is allowed
print(first_tuple[0])  # 1

second_tuple = (0, 9, 19, 39)
print(second_tuple[-1])  # 39


# tuples can be used as keys in dictionaries
locations = {
    (53.5229, 28.329): "Tokyo Office",
    (14.578, 28.329): "New York Office",
    (37.3784, 28.329): "San Francisco Office",
}

locations[(37.3784, 28.329)] # San Francisco Office

cat = {"name": "biscuit", "age": 0.5, "favorite_toy": "Compute keyboard"}
print(cat.items()) # returns a tuple