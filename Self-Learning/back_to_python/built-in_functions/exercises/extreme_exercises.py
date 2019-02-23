#Write a function called extremes. 
# Accepts an iterable. It should return a tuple containing the minimum and maximum elements.

def extremes(iterable):
    if isinstance(iterable, dict):
        return "Sorry I do not have that coded yet"
    if type(iterable) != dict:
        result = (min(iterable), max(iterable))
        return result

# Test Cases
a = [0,23,-1, 39, 1000, 241, 1.3] #(-1, 1000)
b = (99, 23, 4325, 100)  #(23, 4325)
c = "alcatraz" #('a','z)
print(extremes(a))
print(extremes(b))
print(extremes(c))