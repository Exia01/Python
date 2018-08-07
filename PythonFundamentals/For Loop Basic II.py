def test(arr):
    for i in range(0, len(arr)):
        if arr[i] > 0:
            arr[i] = 'big'
    return arr


print(test([-1, -3, 4, -5, 5]))
# biggie size

# def cpositives(arr):
#     temp = 0
#     for i in range(0, len(arr)):
#         if arr[i] > 0:
#             temp += 1
#     arr[len(arr) - 1] = temp
#     return arr


# print(cpositives([1, -1, 1, 1, -2]))


# def stotal(arr):
#     total = 0
#     for i in range(0, len(arr)):
#         total += arr[i]
#     return total


# print(stotal([1, 2, 3, 4, ]))


# def stotal1(arr):
#     print(sum(arr[0:len(arr)]))


# stotal1([1, 2, 3, 4, 1, 1])


def average(arr):
    temp = 0
    for i in range(0, len(arr)):
        temp += arr[i]
    wholenum = temp / len(arr)
    return wholenum
# might get float already may not need to change it


print(average([1, 2, 3, 4]))


# def totalenght(arr):
#     return len(arr)


# print(totalenght([1, 2, 3, 4]))


def minnumb1(arr):
    if (arr): #this means it automatically checks to see if there is anything in there to begin with 
        temp = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < temp:
                temp = arr[i]
        return temp
    else:
        return False


print(minnumb1([1, 5, 3, 4]))


# def minnumb2(arr):
#     print(min(arr))


# minnumb2([8, 6, 2, 4])


# def maxnumb1(arr):
#     print(max(arr))


# maxnumb1([1, 2, 3, 4])


# def maxnumb2(list):
#     temp = list[0]  # cant figure this out
#     for i in range(1, len(list)):
#         if list[i] < temp:
#             temp = list[i]
#     return temp
#     else (len(list) <= 2):
#         return False


# maxnumb1([1, 2, 3, 4])

def minnumb1(arr): #use this to solve max
    if (arr):
        temp = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < temp:
                temp = arr[i]
        return temp
    else:
        return False


print(minnumb1([1, 5, 3, 4]))

