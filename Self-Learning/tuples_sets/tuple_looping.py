months = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December')

for month in months:
    print(month)

cat = {"name": "biscuit", "age": 0.5, "favorite_toy": "Compute keyboard"}
print(cat.items())  # returns a tuple

# using while loop

i = len(months) - 1

while i >= 0:
    print(months[i])
    i -= 1

sample = (1, 2, 3, 3, 5, 6)  # duplicate data is allowed
print(sample.count(3))  # 2

print(sample.index(5))  # index position first matching position

nums = (1, 2, (3, 4), 5, 6, 7)
print(nums[2][0])

print(nums[0:4]) #using slice
print(nums[0:len(nums):2]) #using slice