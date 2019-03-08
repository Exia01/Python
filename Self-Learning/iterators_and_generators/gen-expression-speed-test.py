# Generator Expressions
# easier way of doing them

def nums():
    for num in range(1, 10):
        yield num

g = nums()  #for loop generatoor object

x = (num for num in range(1,10))
print(x) #generator object > generxpr 

import time  # not very precise but this will show a basic approximation



# SUMMING 10,000,000 Digits With Generator Expression
gen_start_time = time.time()  # save start time
print(sum(n for n in range(100000000)))
gen_time = time.time() - gen_start_time  # end time - start time


# SUMMING 10,000,000 Digits With List Comprehension
list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_time = time.time() - list_start_time


print(f"sum(n for n in range(10000000)) took: {gen_time}")
print(f"sum([n for n in range(10000000)]) took: {list_time}")


