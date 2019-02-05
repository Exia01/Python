nested_list = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]

print(nested_list[0][1])  # 2
print(nested_list[1][-1])  # 5
print(nested_list[-1][-1])  # 8
print(nested_list[2][-1])  # 8

for n in nested_list:
    for val in n:
        print(val)

coords = [[10.423, 9.132], [37.1234, -14.093], [21.367, 56.0294]]
for loc in coords:
    print(loc)

testing_ = [[num for num in range(1, 4)] for val in range(1, 3)]

print(testing_)

testing_2 = [["X" if num % 2 != 0 else "O" for num in range(1, 4)] for val in range(1, 4)]
print(testing_2)

testing_3 = [["*" for x in range(1, 4)] for i in range(1, 4)]
print(testing_3)