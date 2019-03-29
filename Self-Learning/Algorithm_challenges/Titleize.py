# Titleize
# Write a function called titleize which accepts a string of words and returns a new string with the first letter of every word in the string
# capitalized.
# # 

def titleize(words):
    temp = words.split()
    result = ' '.join(f'{word[0].upper()}{word[1::]}' for word in temp)
    return result

#Test Cases

print(titleize('this is awesome')) # "This Is Awesome"
print(titleize('oNLy cAPITALIZe fIRSt')) # "ONLy CAPITALIZe FIRSt"