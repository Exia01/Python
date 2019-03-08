# Lame function that returns a list of beats.  
# Only runs 100 times
def current_beat():
	max = 100
	nums = (1,2,3,4)
	i = 0
	result = []
	while len(result) < max:
		if i >= len(nums): i = 0 # if it is 4 reset
		result.append(nums[i])
		i += 1
	return result

# Infinite Generator - returns one beat a time, no list used!
def current_beat():
	nums = (1,2,3,4)
	i = 0
	while True:
		if i >= len(nums): i = 0
		yield nums[i]
		i += 1

print(current_beat())

x = []
for i in range(0, 10):
	x.append(i)

print(x)