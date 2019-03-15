# # you can read a file with open function
# # open returns a file object to you
import os
script_dir = os.path.dirname(__file__)
rel_path = "test.txt"
abs_file_path = os.path.join(script_dir, rel_path)


# print(abs_file_path)
file = open(abs_file_path)
print(file.read())
# print(file.read())  # when called moves the cursor "down a line"
# print(file.read())


# We can use seek to manipulate the location of the cursor
