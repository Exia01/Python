items = [1, 2, 3, 4, 5, 6, ['Hello', 'Testing']]

print(items[1:])
print(items[-1:])
print(items[::-1])# reverses the list 
print(items[-3:]) 

stuff = items[:]  # will copy the array

print(stuff is items)  # share the same memory space?

print(stuff[0:7:2])
print(stuff[7:0:-2])

stuff[:3] = ["A", "B", "C"]
print(stuff)

x =[ "Hello World!", "Testing HEre"]
