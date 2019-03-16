#When writting to a file. We still need to "open" a file
#wether the file exists or not we still the to use the open
#need to specify the "w" flag as the second statement
import os
script_dir = os.path.dirname(__file__)
rel_path = "SecondTest.txt"
abs_file_path = os.path.join(script_dir, rel_path)
#example
with open(abs_file_path, "w") as file:
    file.write("Writting files is great\n")
    file.write("Here's another line of text\n")
    file.write("Closing now, goodbye!\n")

#if we call write again the content will be overwritten

with open(abs_file_path, "a") as file:
    file.write("\nHere's another Haiku\n")
    file.write("The roof, the roof, the roof is on file!\n")
    file.write("Closing now, goodbye!\n")


rel_path = "lol.text"
### You can also write to files that don't yet exist
with open(abs_file_path, "w") as file:
    file.write("haha" * 10000)
