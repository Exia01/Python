# countdown
def countdown(num):
    a = []
    for count in range(num, 0, -1):
        a.append(count)
    print(a)


countdown(100)

# Print and Return


def test(tl):
    print(tl[0])
    return tl[1]


print(test([10, 20]))


# First Plus Length
array = [1, 2, 3, 4]

x = array[0] + len(array)
print(x)

# Values Greater than Second
arr = [9, 3, 5, 6, 7, 8]
newarr = []


def valm(arr):
    for i in arr:
        if len(arr) <= 2:
            print(False)
        if i > (arr[1]):
            newarr.append(i)

    print(newarr)


valm(arr)
arr1 = [3, 4, 5, 6]
arr2 = [8, 9, 4, 6]


def thislenghtthatvalue(arr1, arr2):
    for i in arr2:
        if len(arr1) == i:
            print("Jinx!")
        else:
            print(len(arr1), + i)


thislenghtthatvalue(arr1, arr2)
