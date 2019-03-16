import os
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, "")


class PathFileName:
    def __init__(self, name):
        self.name = name

    def change_name(self, name):
        self.name = name
        return self.name


TempFile = PathFileName("haiku.txt")
file = TempFile.name
abs_file_path = os.path.join(script_dir, file)

# w - writes and erases existing contents
with open(abs_file_path, "w") as file:
    file.write("Here's one more haiku\n")
    file.write("What about the older one?\n")
    file.write("Let's go check it out")

# a - appends to end, preserving original contents
# NO CONTROL OVER CURSOR
with open(abs_file_path, "a") as file:
    file.seek(0)
    file.write(":)\n")

# r+ read and write will work with existing file
with open(abs_file_path, "r+") as file:
    file.write(":)")
    # always start at the beginning and overwrites
    file.seek(10)
    file.write(":(")
    file.seek(5)
    file.write("Spin me right round!")

# file = TempFile.change_name("hello.txt")
# abs_file_path = os.path.join(script_dir, file)

# # r+ will not create a file if it doesn't exist
# with open("hello.txt", "a") as file:
#     file.write("HELLO!!!")
