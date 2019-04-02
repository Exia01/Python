# Write a function called find_greater_numbers which accepts a list and returns the number of times a number is followed by a larger
# number across the entire list.


def find_greater_numbers(vals_list):
    count = []
    list_range = len(vals_list)-1
    if len(vals_list) == 0:
        return 0
    for idx in range(list_range):
        temp_count = 0
        for val in range(idx, list_range):
            if vals_list[idx] < vals_list[val + 1]:
                temp_count += 1
        count.append(temp_count)   
    return sum(count)


# Test Cases

print(find_greater_numbers([1, 2, 3]))  # 3
print(find_greater_numbers([6, 1, 2, 7]))  # 4
print(find_greater_numbers([5, 4, 3, 2, 1]))  # 0
print(find_greater_numbers([]))  # 0
