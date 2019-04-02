# Write a function called find_greater_numbers which accepts a list and returns the number of times a number is followed by a larger
# number across the entire list. 

def find_greater_numbers(vals_list):
    count = 0
    if len(vals_list) > 0:
        for idx in range(1,len(vals_list)):
            if vals_list[idx - 1] > vals_list[idx]:
                count += 1
    return count



#Test Cases

print(find_greater_numbers([1,2,3])) # 3 
print(find_greater_numbers([6,1,2,7])) # 4
print(find_greater_numbers([5,4,3,2,1])) # 0
print(find_greater_numbers([])) # 0