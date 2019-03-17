# find_and_replace
# Write a function called nd_and_replace, which takes in a file name, a word to search for, and a replacement word. Replaces all instances
# of the word in the file with the replacement word.

from pathlib import Path
data_folder = Path(
    "c:/Users/sixgg/Documents/GitHub/Python/Self-Learning/File IO/exercise/find_and_replace/")
filename = "story.txt"
file=data_folder / filename

def find_and_replace(og_file, old_word, new_word, file=file):
    with open(file, "r+") as f:  # opening file
        text = f.read()
        new_text = text.replace(old_word, new_word)
        f.seek(0)
        f.write(new_text)
        f.truncate()
        

find_and_replace('story.txt', 'Alice', 'Jose') 
