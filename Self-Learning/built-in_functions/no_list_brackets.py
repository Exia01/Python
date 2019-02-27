# We don't necessarily need to include the brackets, becomes a generator expression
#example
people = ['Charlie', 'Casey', 'Cody', 'Carly', 'Christina']
result = [name[0] == 'C' for name in people]
print(result)
print(all(name[0] == 'C' for name in people))

# More information here:
#https://stackoverflow.com/questions/47789/generator-expressions-vs-list-comprehension/47826#47826