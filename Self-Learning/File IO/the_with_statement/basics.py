# # you can read a file with open function
# # open returns a file object to you
import os
script_dir = os.path.dirname(__file__)
rel_path = "test.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as file:  # can be any name instead of file
    print(file.read())  #file will close automatically
    
#the interface for these with statements will be called 
#when called f.__enter__() 
#when called f.__exit__() 