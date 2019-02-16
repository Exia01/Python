# write a function called list_manipulation.
# Should take in four parameters. A list, command. location, value
# if the command is to "remove" and the location is "end", the function should remove the last value in the list
# if the command is to "remove" and the location is "beginning", the function should remove the first value in the list
# if the command is to "add" and the location is "end", the function should add the value last in the list
# if the command is to "add" and the location is "beginning", the function should add the value first  in the list

list = [1, 2, 3, 4, 5, 6]
command = "remove"
location = "beginning"
value = 5000


def list_manipulation(*args):
    if 'add':
        if location == "end":
            list.append(value)
            return list
        elif location == "beginning":
            list.insert(0, value)
            return list
    else:
        if location == "end":
            list.pop()
            return list
        elif location == "beginning":
            list.pop(0)
            return list


#test cases
list_sample2 = [6, 7, 8, 9, 10]
value =1500
command = "add"
location  = "end"

print(list_manipulation(list, command, location, value))

list = [1, 2, 3, 4, 5, 6]
command = "remove"
location = "beginning"
value = 5000

print(list_manipulation(list, command, location, value))

#Another way of doing insert
def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection