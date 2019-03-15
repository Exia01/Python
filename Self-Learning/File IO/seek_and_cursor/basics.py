# # you can read a file with open function
# # open returns a file object to you
import os
script_dir = os.path.dirname(__file__)
rel_path = "test.txt"
abs_file_path = os.path.join(script_dir, rel_path)
# print(abs_file_path)
file = open(abs_file_path)
# print(file.read())  # when called moves the cursor "down a line"

print(file.seek(0))
print(file.readline())  #one line at a time

print(file.readlines())  # all the lines preserved as all the lines in a list

print(file.close) #false
file.close()  #can't be read again till you open it again
print(file.close) #true
# # directory help
# # https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python/7166139
