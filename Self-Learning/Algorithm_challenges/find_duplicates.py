# Write a function called find_the_duplicate which accepts an array of numbers containing a single duplicate. The function returns the
# number which is a duplicate or None if there are no duplicates.

def find_the_duplicate(list):
    temp_set = set(list)
    for num in list:
        try:
            temp_set.remove(num)
        except KeyError:
            return num
    return None

#Test Cases:
print(find_the_duplicate([1,2,1,4,3,12])) # 1
print(find_the_duplicate([6,1,9,5,3,4,9])) # 9
print(find_the_duplicate([2, 1, 3, 4]))  # None


#another way
def _find_the_duplicate(arr):
    counter = {}
    for val in arr:
        if val in counter:
            counter[val] += 1
        else:
            counter[val] = 1
    for key in counter.keys():
        if counter[key] > 1:
            return int(key)