#abs --> Returns the absolute value of a number. The argument may be an integer or a floating point number

#Example
print(abs(5))  #5 
print(abs(3.5555555))
print(abs(-1324934820.39248))

import math
print(math.fabs(-3923))  #treats everything as a float

#Sum
#takes an iterable and an optional start
# returns the sum of start and the items of an iterable from left to right and returns the total.
# starts default to 0

print(sum([1,2,3]))
print(sum([1, 2, 3,], 10))  # will start at 10 and add

#round 
#Return number rounded to ndigits precision after the decimal point. 
#If ndigits is omitted or is None, it returns the nearest integer to input
print(round(10.2))  #10
print(round(1.24323492834, 2))#1.24