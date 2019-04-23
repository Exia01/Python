# Write a function called mode.This function accepts a list of numbers and returns the most frequent number in the list of numbers

def mode(nums_list):
    temp_frequency = 0
    result = 0
    # can implement checks HeaderError
    temp_generator = dict((k, nums_list.count(k)) for k in nums_list)
    for key, value in temp_generator.items():
        if temp_frequency < value:
            temp_frequency = value
            result = key

    return result
#Test Cases
print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4])) # 4

# Refractored solution
def mode_r(collection):
    count = {val: collection.count(val) for val in collection}
    # find the highest value (the most frequent number)
    max_value = max(count.values())
    # now we need to see at which index the highest value is at
    correct_index = list(count.values()).index(max_value)
    # finally, return the correct key for the correct index (we have to convert cou)
    return list(count.keys())[correct_index]