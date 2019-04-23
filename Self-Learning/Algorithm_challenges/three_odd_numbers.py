# three_odd_numbers
# Write a function called three_odd_numbers, which accepts a list of numbers and returns True   if any three consecutive numbers sum to an odd number.

def three_odd_numbers(nums_list, window_size=3):
    n = window_size
    results = []
    temp_sum = 0
    #test this check
    if window_size > len(nums_list):
        return False
    # first sum
    for i in range(window_size):
        temp_sum += nums_list[i]
    
    #can implement quick short circuit here
    results.append(temp_sum % 2 != 0)
    
    for i in range(window_size, len(nums_list)):
        temp_sum = temp_sum - nums_list[i - n] + nums_list[i]
        results.append(temp_sum % 2 != 0)
    return any(results)
    
##Test Cases

print(three_odd_numbers([1,2])) # True
print(three_odd_numbers([1,2,3,4,5])) # True
print(three_odd_numbers([0,-2,4,1,9,12,4,1,0])) # True
print(three_odd_numbers([5,2,1])) # False
print(three_odd_numbers([1,2,3,3,2])) # False



#Here be dragons
# https://scipher.wordpress.com/2010/12/02/simple-sliding-window-iterator-in-python/






# def maxSubArraySum(arr, n):
#     tempSum = 0
#     maxSum = 0

#     dic = {}
#     try:
#         n > len(arr)
#     except:
#         return None
#     for num in range(n):
#         maxSum += arr[num]
#     # print(maxSum)

#     tempSum = maxSum
#     for i in range(n, len(arr)):
#         # print(arr[i-n], arr[i], tempSum)
#         tempSum = tempSum - arr[i - n] + arr[i]
#         maxSum = max(maxSum, tempSum)
#         # if (tempSum > maxSum):
#         #     maxSum = tempSum
#     return maxSum


# print(maxSubArraySum(arr, n))
