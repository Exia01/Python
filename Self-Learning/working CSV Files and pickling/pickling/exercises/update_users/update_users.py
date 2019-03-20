# update_users

# Implement the following function:
# update_users  : Takes in an old first name, an old last name, a new first name, and a new last name. Updates the  users.csv file so that
# any user whose first and last names match the old first and last names are updated to the new first and last names. The function should
# return a count of how many users were updated.
'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''
import pickle
from csv import reader, writer
from pathlib import Path

data_folder = Path(
    r'C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\working CSV Files and pickling\pickling\exercises\update_users')
filename = "users.csv"
# generates an instance each time it is used
file = data_folder / filename
pickle_file = data_folder / "update_user.pickle"


def update_users(*args):
    first = args[0]
    last = args[1]
    replace_first = args[2]
    replace_last = args[3]
    count = 0
    with open(file, "r") as csv_file:
        temp_csv = list(reader(csv_file, delimiter=','))
        for names in temp_csv:
            if first in names and last in names:
                names[0] = replace_first
                names[1] = replace_last
                count += 1
        with open(file, "w") as f1:
            cvs_writer = writer(f1, lineterminator="\n")
            for row in temp_csv:
                cvs_writer.writerow(row)

    return "Users updated: {}.".format(count)


print(update_users("Colt", "Steele", "Boba", "Fett"))



#another way of doing it:
import csv
 
def _update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
 
    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)
 
    return "Users updated: {}.".format(count)