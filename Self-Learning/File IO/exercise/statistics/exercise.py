# statistics
# Write a function called statistics, which takes in a le name and returns a dictionary with the number of lines, words, and characters in
'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''
from pathlib import Path
data_folder = Path(
    "c:/Users/sixgg/Documents/GitHub/Python/Self-Learning/File IO/exercise/statistics/")
filename = "story.txt"
file = data_folder / filename

def statistics(filename):
    dict = {}
    lines = 0
    words = 0
    characters = 0
    with open(file) as f:  # opening file
        for line in f:
           wordsList = line.split()
           lines += 1
           words += len(wordsList)
           characters += len(line) #the 
    dict["lines"] = lines
    dict["characters"] = characters
    dict["words"] = words
    return dict
print(statistics(file))


#more optimized way of doing it
def _statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()
 
    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }