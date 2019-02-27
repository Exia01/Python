def sum_all_values(*args):
	print(args) # print all values as a tuple
	total = 0
	for num in args:
		total += num
	print(total)

sum_all_values(1,30,2,5,6) # this works

nums = [1, 2, 3, 4, 5, 6]
#without the * would through error 
# ([1, 2, 3, 4, 5, 6],) this is what is passing
# By adding the start we pass each number as individual argument 
sum_all_values(*nums) #without the * would through error

example = {
	'a': 1,
	'b':2
}
def print_packed(**kwargs):
	print(kwargs) # print all values as a tuple
	total = 0
	for num in kwargs.values(): # or we can use items
		total += num
	return(total)

print(print_packed(**example)) #unpacking dictionaries