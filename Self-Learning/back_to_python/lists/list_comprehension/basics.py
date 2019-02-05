nums = [1, 2, 3, 4, 5]

squared_nums = [x*x for x in nums]

print(squared_nums)

greeting = "Hello World!"

all_caps = [char.upper() for char in greeting]  # not the washington caps
print(all_caps)

example1 = [num * 10 for num in range(1, 6)]
print(example1)

example2 = [bool(val) for val in [0, [], '']]
print(example2)  # will print the boolean value of those 

string_nums = [str(num) for num in nums]
print(string_nums)
