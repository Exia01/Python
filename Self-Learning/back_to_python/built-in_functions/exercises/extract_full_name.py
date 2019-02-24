# write a function called "extract_full_name"
# Function should accept a list of dictionaries and return a new list of strings with the first and last name keys in each dictionary concatenated


def extract_full_name(names):
    if not names:
        return None
    test = list(map(lambda l: f'{l.get("first", None)} {l.get("last", None)}', names))
    return test
# Test cases
names = [
    {'first': 'Elie', 'last': 'Schoppik'},
    {'first': 'John', 'last': 'Connor'},
    {'first': 'Barbara', 'last': 'o\'Connor'},
    {'first': 'Batman', 'last': ""},
]

print(extract_full_name(names))  # ['Elie Schoppik', John Connor']


def another_extract_full_name(names):
    if not names:
        return None
    first = (d['first'] for d in names)
    test = zip(first, map(lambda l: l['last'], names))
    result = [" ".join(l) for l in test if not None in l]
    return result

# Test cases
names = [
    {'first': 'Elie', 'last': 'Schoppik'},
    {'first': 'John', 'last': 'Connor'},
    {'first': 'Barbara', 'last': 'o\'Connor'},
    {'first': 'Batman', 'last': None},
]

print(extract_full_name(names))  # ['Elie Schoppik', John Connor']


# One liner Basically
def _extract_full_name(dic):
    return list(map(lambda x: x['first'] + " " + x["last"], dic)) 