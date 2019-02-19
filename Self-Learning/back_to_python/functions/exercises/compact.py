# Write a function called "compact"
#function accepts a list and returns  a list of values that are truthy without falsey

def compact(list=None):
    if list:
        result = [val for val in list if val]
        return result

print(compact([0,1,2,"",[],False,{},None,"All done"]))