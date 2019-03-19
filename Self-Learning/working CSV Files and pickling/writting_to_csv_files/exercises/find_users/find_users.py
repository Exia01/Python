# find_user
# Use users.csv  . Each row of data consists of two columns: a user's first name, and a
# user's last name.

# find_user  : Takes in a frst name and a last name and searches for a user with that frst and last name in the  users.csv  file. If the user is
# found,  find_user   returns the index where the user is found. Otherwise it returns a message stating that the user wasn't found
from csv import reader, DictReader
from pathlib import Path

data_folder = Path(
    r"C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\working CSV Files and pickling\writting_to_csv_files\exercises\find_users")
filename = "users.csv"
file = data_folder / filename  # generates an instance each time it is used


def find_user(first_name, last_name, file=file):
    with open(file) as csvfile:
        cvs_reader = DictReader(csvfile)
        name = f'{first_name} {last_name}'
        for count, row in enumerate(cvs_reader):
            temp_name = ('{} {}'.format(row.get('First Name', "Not Found"),row.get('Last Name', "Not Found")))
            if name == temp_name:
                print(count)
                break
        return "{} not found.".format(name)
print(find_user("Jimmy", "blah"))


# Another way of doing it
