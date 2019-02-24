#write a function "max_magnitude"
#Accepts a single list full of numbers. 
#Returns the magnitude of the number with the largest magnitude.

def max_magnitude(l):
    templist = (abs(val) if val < 0 else val for val in l)
    return max(templist)

#Test cases
print(max_magnitude([300,20,-900]))# 900
print(max_magnitude([10,11,12]))  #12
print(max_magnitude([-1, -5, -89]))  # 89


#Refractored
def r_max_magnitude(nums):
    return max(abs(num) for num in nums)