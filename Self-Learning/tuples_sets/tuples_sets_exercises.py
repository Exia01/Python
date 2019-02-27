# Tuples and Sets exercise

numbers = (1, 2, 3, 4)

value = (1,)  # single value tuple
#creating a tuple from list 
values = [10, 20, 30]
tuple_vals = tuple(values)
tuple_vals2 = *values, #another way of creating a tuple
tuple_vals3 = (*values,)#another way of creating a tuple
#This essentially unpacks the list l inside a tuple literal which is created due to the presence of the single comma ,

print(value)
print(tuple_vals)


#creating a set from a list
stuff = [1, 3, 1, 5, 2, 5, 1, 2, 5]
sample = set(stuff) #f you have a list of hashable objects or iterable 
print(numbers)
print(value)
print(tuple_vals)
