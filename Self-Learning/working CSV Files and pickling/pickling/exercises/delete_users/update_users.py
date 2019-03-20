# delete_users

# Implement the following function:
# delete_users  : Takes in a first name and a last name. Updates the  users.csv  file so that any user whose first and last names match the
# inputs are removed. The function should return a count of how many users were removed.

import csv
import pickle
from csv import reader, writer
from pathlib import Path

data_folder = Path(
    r'C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\working CSV Files and pickling\pickling\exercises\delete_users')
filename = "users.csv"
# generates an instance each time it is used
file = data_folder / filename


def delete_users(*args):
    first = args[0]
    last = args[1]

    count = 0
    with open(file, "r") as csv_file:
        temp_csv = list(reader(csv_file, delimiter=','))

        with open(file, "w") as f1:
            cvs_writer = writer(f1, lineterminator="\n")
            for names in temp_csv:
                if first not in names and last not in names:
                    cvs_writer.writerow(names)
                else:
                    count +=1

    return "Users deleted: {}.".format(count)


print(delete_users("Colt", "Steele")) # Users deleted: 2.
