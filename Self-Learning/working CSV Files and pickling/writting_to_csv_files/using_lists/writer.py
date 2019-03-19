#writer creates a writer object for writting to csv
from csv import writer, DictWriter
from pathlib import Path
# Version using writer
data_folder = Path(
    r"C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\working CSV Files\writting_to_csv_files")
filename = "cats.csv"
file = data_folder / filename
with open(file, "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["Blue", 3])
    csv_writer.writerow(["Kitty", 1])

""" # Version using DictWriter
with open(file, "w") as file:
	headers = ["Name", "Breed", "Age"]
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	csv_writer.writerow({
		"Name": "Garfield",
		"Breed": "Orange Tabby",
		"Age": 10
	})
 """