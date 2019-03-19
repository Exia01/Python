# For this exercise, you'll be working with a file called  users.csv. Each row of data consists of two columns: a user's first name, and a
# user's last name.
# Implement the following function:
# print_users  : prints out all of the first and last names in the  users.csv  file

from csv import reader, DictReader
from pathlib import Path

data_folder = Path(
    r"C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\working CSV Files\writting_to_csv_files\exercises\print_users")
filename = "users.csv"
file = data_folder / filename  # generates an instance each time it is used


def print_users(file=file):
    with open(file) as f:
        cvs_reader = DictReader(f)
        # data = list(cvs_reader)
        # data = DictReader(cvs_reader)
        for row in cvs_reader:
            print(row.get('First Name', "Not Found"),
                  row.get('Last Name', "Not Found"))


print(print_users())



# Another way of doing it
import csv
 
def print_users():
    with open("users.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader: 
            print("{} {}".format(row['First Name'], row['Last Name']))