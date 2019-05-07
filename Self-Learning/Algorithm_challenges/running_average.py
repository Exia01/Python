# running_average
# Create a function running_average that returns a function. When the function returned is passed a value, the function returns the
# current average of all previous function calls. look to use closure to solve this. You should round all answers to the 2nd decimal place.
import math


def running_average():
    running_average.hello = "Hi"
    temp_arr = []

    def temp_function(num):
        temp_arr.append(num)
        return round(sum(temp_arr)/len(temp_arr), 2)
    return temp_function


# Test Cases:
rAvg = running_average()  # no default param
print(rAvg(10))  # 10.0
print(rAvg(11))  # 10.5
print(rAvg(12))  # 11

rAvg2 = running_average()
print(rAvg2(1))  # 1
print(rAvg2(3))  # 2

# using closure: https://stackoverflow.com/questions/4020419/why-arent-python-nested-functions-called-closures
# explanation:https://www.youtube.com/watch?v=swU3c34d2NQ


#using attributes
def Rerunning_average():
    Rerunning_average.accumulator = 0
    Rerunning_average.size = 0
  
    def inner(number):
        Rerunning_average.accumulator += number
        Rerunning_average.size += 1
        return Rerunning_average.accumulator / Rerunning_average.size
    
    return inner