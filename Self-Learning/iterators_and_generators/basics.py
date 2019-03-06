name = "Oprah"

# next(name)  #error 'str' object is not an iterator

iter_name = iter(name)
print(iter_name)

print(next(iter_name))
print(next(iter_name))
print(next(iter_name))

nums = [1, 2, 3, 4, 5,]
# next(nums) # 'list' object is not an iterator
iter_num = iter(nums)
print(next(iter_num))
print(next(iter_num))
print(next(iter_num))