
# 1 copy('story.txt', 'story_copy.txt')
# 2 # expect the contents of story.txt and story_copy.txt to be the same
from pathlib import Path
data_folder = Path(
    "c:/Users/sixgg/Documents/GitHub/Python/Self-Learning/File IO/exercise/copy_and_reversed/")
filename = "story.txt"
file=data_folder / filename

def copy_and_reverse(og_file, copy_file_name, file=file):
    with open(file) as f:  # opening file
        doc = f.readlines()
        doc = reversed(doc)
        file = data_folder / "story_reversed.txt"
        with open(file, "w") as f1:  # second file
            for line in doc:
                line = line[::-1]
                f1.write(line)
              # for line in doc:
              #   f1.write(line)

copy_and_reverse('story.txt', "story_reversed.txt")


# https://stackoverflow.com/questions/529424/traverse-a-list-in-reverse-order-in-python

#another way def copy_and_reverse(file_name, new_file_name):
#     with open(file_name) as file:
#         text = file.read()
 
#     with open(new_file_name, "w") as new_file:
#         new_file.write(text[::-1])