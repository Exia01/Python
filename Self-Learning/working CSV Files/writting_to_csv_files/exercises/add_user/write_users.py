# add_user
# create users.csv  . Each row of data consists of two columns: a user's rst name, and a
# user's last name.
# Implement the following function:
# add_user  : Takes in a first name and a last name and adds a new user to the  users.csv file


from csv import writer, DictWriter
from pathlib import Path

data_folder = Path(
    r"C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\working CSV Files\writting_to_csv_files\exercises\add_user")
filename = "users.csv"
file = data_folder / filename  #generates an instance each time it is used

def add_user(first_name, last_name_, file=file):
    with open(file, "a") as f:
        headers = ('First Name', 'Last Name')
        cvs_writer = DictWriter(f, fieldnames=headers)
        # cvs_writer.writeheader()
        cvs_writer.writerow({
            "First Name": first_name,
            "Last Name": last_name_
        })


add_user("Jose", "gonzalez")