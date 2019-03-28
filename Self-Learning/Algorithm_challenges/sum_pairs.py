# Write a function called sum_pairs which accepts a list and a number and returns the first pair of numbers that sum to the number passed
# to the function

def sum_pairs(val_list, num):
    x = 1
    list_length = len(val_list) - 1
    for index in range(list_length):
        temp_sum = val_list[index] + val_list[x]
        if temp_sum == num:
            return  [val_list[index], val_list[x]]
        x += 1
    return []

        

#Test Cases
print(sum_pairs([4,2,10,5,1], 6)) # [4,2]
print(sum_pairs([11,20,4,2,1,5], 100)) # []