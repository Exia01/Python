# Write a function called remove_every_other that accepts a list and returns a new list with every second value removed.
def remove_every_other(list_val, index=1):
    """ Takes in list and removes second value """
    list_length = len(list_val)
    new_list = []
    if list_length > 1:
        for index in range(0,list_length, 2):
            new_list.append(list_val[index])
        return new_list
    return list_val

#Test Cases
print(remove_every_other([1,2,3,4,5])) # [1,3,5] 
print(remove_every_other([5,1,2,4,1])) # [5,2,1]
print(remove_every_other([1])) # [1] 