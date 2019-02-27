l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, l))
print(evens)


# Yet another example
names = ["austin", "penny", "anthony", "angle", "billy"]
a_names = list(filter(lambda n: n[0] == 'a', names))
print(a_names)


# combining filter and maps
sample = ['Lassie', "Timothy", 'Joe', 'Tim']

combined = list(map(lambda n: f'Your instructor is {n}', filter(
    lambda value: len(value)<5, sample)))

print(combined)


#More complicated
users = [
    {"username": "samuel", "tweets": [
        "I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]
# extract inactive users using filter:
inactive_users = list(filter(lambda u: not u['tweets'], users))
# check if tweets property is empty, if it is add it
print(inactive_users)
# extract inactive users using list comprehension:
inactive_users2 = [user for user in users if not user["tweets"]]
print(inactive_users2)


# extract usernames of inactive users w/ map and filter:
usernames = list(map(lambda user: user["username"].upper(),
                     filter(lambda u: not u['tweets'], users)))
print(usernames)
# extract usernames of inactive users w/ list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]
print(usernames2)
