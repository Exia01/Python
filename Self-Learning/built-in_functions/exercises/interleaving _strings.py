# A difficult challenge.
#Write a function that accepts two stings. It should return a new string containing the 2 string intervowen or zipped together. 
#Example:
    # interleave('hi', 'ha') #hhia
    #interleave('aaa', 'zzz') #'azazaz'

def interleave(string1, string2):
    if not string1 or not string2:
        return None
    temp = "".join(["".join(str) for str in (zip(string1, string2))])
    return temp
    

#Test Cases
print(interleave('hi', 'ha'))  #hhia

print(interleave('aaa', 'zzz')) #'azazaz'
print(interleave('hi', 'no')) #'azazaz'