# sorted will work with other iterable collections like tuples and list. We can also pass a lambda for dictionary with keys within objects

sample = [6, 98, 324, 23, 11, 1]

result = sorted(sample)  # sample however has not change, returns copy

print(result)

# can also pass in a tuple, stills returns a list
x = sorted((2, 1, 45, 23, 9))
print(x)

# what if it is a list of dictionary
users = [
    {'username': 'samuel', 'tweets': [
        'I love cake', 'I love pie', 'hello world!']},
    {'username': 'katie', 'tweets': ['I love my cat']},
    {'username': 'jeff', 'tweets': [], 'color':'Purple'},
    {'username': 'bob123', 'tweets': [], 'num':10, 'color':'teal'},
    {'username': 'doggo_luvr', 'tweets': ['dogs are the best', 'I\'m hungry']},
    {'username': 'guitar_gal', 'tweets': []}
]

# can't do this
# sorted(users)

# can do this
sample2 = sorted(users, key=len)

# this will sort it based on the length of the "keys" meaning how many keys per dictionary
print(sample2)

explanation_before = map(lambda user: user['username'], users)
print(list(explanation_before))
# meaning it is going to sort based of the key for each user?
sample3 = sorted(users, key=lambda user: user['username'])

# Here be dragons essentially is it looping through the users, by the keys provided by the lambda
print(sample3)


sample4 = sorted(users, key=lambda user: len(user['tweets']))
sample4 = sorted(users, key=lambda user: len(
    user['tweets']), reverse=True)  # can reverse
# this will sort based on the length returned by the lambda

# returns it based on the tweets
print(sample3)

# ANOTHER
songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# To sort songs by playcount
print(sorted(songs, key=lambda s: s['playcount']))
print(sorted(songs, key=lambda s: s['playcount']), reversed="True")
