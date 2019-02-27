# Create a dictionary with the Character letters using chr() in python from numbers 65-90

start = 65
end = 91


abc_list = {num: chr(num) for num in range(start, end)}
print(abc_list)
