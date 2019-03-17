# Write a function called copy, which takes in a le name and a new le name and copies the contents of the rst le to the second le.
# (Note: we've provided you with the rst chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is
# also the text used in the tests.
# 1 copy('story.txt', 'story_copy.txt')
# 2 # expect the contents of story.txt and story_copy.txt to be the same
from pathlib import Path
data_folder = Path(
    "c:/Users/sixgg/Documents/GitHub/Python/Self-Learning/File IO/exercise/copy_task/")
filename = "story.txt"
file=data_folder / filename

def copy(og_file, copy_file_name, file=file):
    with open(file) as f:  # opening file
        file = data_folder / "story_copy.txt"
        with open(file, "w") as f1:  # second file
            for line in f:
                f1.write(line)
                # Each line in the file is iterated over using a for loop (in the input stream)

copy('story.txt', 'story_copy.txt')
