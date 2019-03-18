from csv import DictReader
from csv import reader
from pathlib import Path
data_folder = Path(
    r"c:\Users\sixgg\Documents\GitHub\Python\Self-Learning\working CSV Files")
filename = "fighters.csv"
file = data_folder / filename
# THIS DOES READ THE FILE BUT IT DOESN'T PARSE IT!
# BAD!!!!!!
""" with open(file) as f:
    data = f.read()
    print(data)

 """
# using reader
with open(file) as f:
    csv_reader = reader(f)  # reader object like a generator
    for row in csv_reader:
        print(f'{row[0]} is from {row[1]}')
        # each row in a list!
        print(row)

# another way
with open(file) as f:
    csv_reader = reader(f)  # reader object like a generator
    data = list(csv_reader)
    print(data)

# Using DictReader
with open(file) as f:
    csv_reader = DictReader(f)
    for row in csv_reader:
        # each row is an OrderedDict!
        print(row)
        print(row.get('Name', "Not Found"))

file = data_folder / "fighters2.csv"
#Delimited format
with open(file) as f:
    csv_reader = reader(f, delimiter="|") #can be any delimiter
    for row in csv_reader:
        # each row is an OrderedDict!
        print(row)
        # print(row.get('Name', "Not Found"))
