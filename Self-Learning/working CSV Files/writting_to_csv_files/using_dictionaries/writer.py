#writer creates a writer object for writting to csv
from csv import writer, DictWriter
from pathlib import Path
# Version using writer
data_folder = Path(
    r"C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\working CSV Files\writting_to_csv_files/using_dictionaries")
filename = "cats.csv"
file = data_folder / filename

# Version using DictWriter
with open(file, "w") as f:
	headers = ["Name", "Breed", "Age"]
	csv_writer = DictWriter(f, fieldnames=headers) #file and headers
	csv_writer.writeheader()# will write the headers
	csv_writer.writerow({
		"Name": "Garfield",
		"Breed": "Orange Tabby",
		"Age": 10
	})
