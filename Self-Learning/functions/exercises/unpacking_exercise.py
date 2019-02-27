# with the given function call it twice
def count_sevens(*args):
    return args.count(7)

#first time pass arguments 1,2,4 or 1,4,7 second time pass the list below:
nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]


result1 = count_sevens(1,2,3)

result2 = count_sevens(*nums)

print(result1)
print(result2)



#another example :
def addition(x,y):
    return x+y
def sum_numbers(fn = addition,**kwargs):
    final_sum = 0
    for key, num in kwargs.items():
        if isinstance(num, list):
            num_list = num
            tempsum = sum(num_list)
            final_sum += addition(tempsum, final_sum)
        else:
            final_sum += num
    return final_sum


totals = {
    'first': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
    'second':[100,1000],
    }

dict1 = {
    'a': 1,
    'b': 2,
}
result3 = sum_numbers(**dict1)

result4 = sum_numbers(**totals)

print(result3)
print(result4)




