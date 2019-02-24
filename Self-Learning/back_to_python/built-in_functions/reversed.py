# returns a reversed iterator
example1 = [99, 88, 32, 21, 1]
print(example1.reverse())

# we can also have a reverse object
x = reversed(example1)
print(x)

# we could then do a forloop
for num in x:
    print(num*num)

# or do this 
y = example1[::-1]

# we can also use it in a range
for x in reversed(range(0, 10)):
    print(x)

# Reversed does not work on a dictionary, but there are still ways of inverting a dictionary.  If you want to switch the keys and values, you could do it with this one liner:
data = {}
{v: k for k, v in data.items()}

#if we want to reverse keys we can put them in a list
dic = {'a': 1,'b': 4, 'c': 6}
original = [k for k in dic.keys()]
print(original)
second_list = original.reverse()
third_list = list(reversed(original))
 
print(original)
print(second_list)
print(third_list)