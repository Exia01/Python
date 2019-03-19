# writer creates a writer object for writting to csv
from csv import writer, DictWriter
from csv import reader, writer
from pathlib import Path
# Version using writer
data_folder = Path(
    r"C:\Users\sixgg\Documents\GitHub\Python\Self-Learning\working CSV Files\writting_to_csv_files")
filename = 'fighters.csv'
file = data_folder / filename
file2= data_folder / 'screaming_fighters.csv'


# using nested with statements
with open(file) as f:
    csv_reader = reader(f)  # data never converted to list
    #if done separate closes the file
    with open(file2, "w") as f1:
        csv_writer = writer(f1)
        for fighter in csv_reader:
            print(fighter)
            csv_writer.writerow([s.upper() for s in fighter])



# # Other approach, with only 1 file open at a time
# with open(file) as f:
#     csv_reader = reader(f)
#     # data converted to list and saved to variable
#     fighters = [[s.upper() for s in row] for row in csv_reader]

# with open(file2, "w") as file:
#     csv_writer = writer(file)
#     for fighter in fighters:
#         csv_writer.writerow(fighter)
