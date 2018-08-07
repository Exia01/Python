
# somelist = [1, 12, 2, 53, 23, 6, 17]
# max_value = max(somelist)
# min_value = min(somelist)
# avg_value = sum(somelist) / len(somelist)
# If you want to manually find the minimum as a function:

# somelist = [1, 12, 2, 53, 23, 6, 17]


# def my_min_function(somelist):
#     min_value = None
#     for value in somelist:
#         if not min_value:
#             min_value = value
#         elif value < min_value:
#             min_value = value
#     return min_value


'''Python 3.4 introduced the statistics package, which provides mean and additional stats:'''

# from statistics import mean, median

# somelist = [1, 12, 2, 53, 23, 6, 17]
# avg_value = mean(somelist)
# median_value = median(somelist)

# words = "It's thanksgiving day. It's my birthday,too!"
# print(words)
# words.find('day')

# words.replace('day', 'month', 1)
# print(words)
# x = [2, 54, -2, 7, 12, 98]
# print(x)
# print(max(x), min(x))
# x1 = ["hello", 2, 54, -2, 7, 12, 98, "world"]
# print(x1[0], x1[-1])

# for i in range(1, 100):
#     if i % 5 == 0:
#         print('Coding', i)
#     if i % 10 == 0:
#         print('Dojo', i)
#     else:
#         print(i)


def a():
    b = 100
    print(b)
    if b < 10:
        return 5:
    else:
        return 10
        return 7

print(a)
