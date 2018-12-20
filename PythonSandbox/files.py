# Python has functions for creating, reading, updating, and deleting files.

# Open a file and can also create it
myFile = open('myfile.txt', 'w') # w leaves it open

# Get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
# write will continuously write to it
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
# a is appending otherwise it'll overwrite to it
myFile.write(' I also like PHP')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)
