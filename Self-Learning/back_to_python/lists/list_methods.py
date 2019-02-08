#methods and functions in python
# these functions are specific to lists --> "lists methods "
items = [1, 2, 3, 4, 'socks', 'vortex', 'socks', [1,2]]

#add
items.append(5)  # will add 5 to the end
correct_list = [1, 2, 3, 4]
correct_list.extend([5, 6])
print(correct_list)


list_inserting = [1, 2, 3, 4]
# passing in the index we want to add data to 
list_inserting.insert(2, 'Ellow!')
list_inserting.insert(len(list_inserting), "Last")
print(list_inserting)


#swapping values
names = ["James", "Michelle"]
names[0], names[1] = names[1], names[0]