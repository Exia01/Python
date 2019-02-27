#write a function called "partition"
#This function accepts a list and a callback function which assumes returns tru or false

#The function should iterate over each element in the list and invoke the callback function at each iteration

# the result should be a list made of two list, [truthy or falsey] list 

list = [1,2,3,4]
def isEven(num):
    return num % 2 == 0

def partition(list=None, fn=isEven):
    truthy = []
    falsey = []
    result = [truthy, falsey]
    for num in list:
        if isEven(num):
            truthy.append(num)
        else:
            falsey.append(num)
    return result


print(partition(list, isEven))  # [[2,4],[1,3]]


#Another way of doing it, though it is less readable 
def partition_2(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]] # both are created under one array or "list"