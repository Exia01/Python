from csv import DictReader, DictWriter
from pathlib import Path
data_folder = Path(
    r"C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\working CSV Files\writting_to_csv_files/using_dictionaries")
filename = "fighters.csv"
file = data_folder / filename
def cm_to_in(cm):
	return float(cm) * 0.393701

with open(file) as f:
	csv_reader = DictReader(f)
	fighters = list(csv_reader)

file = data_folder / "inches_fighters.csv"
with open(file, "r+") as f:
	headers = ("Name","Country","Height")
	csv_writer = DictWriter(f, fieldnames=headers)
	csv_writer.writeheader() #writes the headers
	for f in fighters:
		csv_writer.writerow({
			"Name": f["Name"],
			"Country": f["Country"],
			"Height": cm_to_in(f.get("Height (in cm)", 0.0))
		})


#Another way
import csv
 
def _add_user(first_name, last_name):
    with open("users.csv", "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([first_name, 