# Write a function called range_in_list which accepts a list and start and end indices, and returns the sum of the values between (and
# including) the start and end index.
# If a start parameter is not passed in, it should default to zero. If an end parameter is not passed in, it should default to the last value in the
# list.Also, if the end argument is too large, the sum should still go through the end of the list.

def range_in_list(val_list, start=None, end=None):
    if len(val_list) == 0:
        return 0
    if end:
        return sum(val_list[start:end+1])
    elif start:
        return sum(val_list[start::])
    else:
        return sum(val_list)





# Test Cases
print(range_in_list([1,2,3,4],0,2))#  6
print(range_in_list([1,2,3,4],0,3))# 10
print(range_in_list([1,2,3,4],1))#  9
print(range_in_list([1,2,3,4]))# 10
print(range_in_list([1,2,3,4],0,100))# 10
print(range_in_list([], 0, 1))  # 0


#here be dragons
def _range_in_list(lst, start=0, end=None):
    end = end or lst[-1]
    return sum(lst[start:end+1])