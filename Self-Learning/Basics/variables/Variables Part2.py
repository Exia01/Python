a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# you can break up expressions
c = a+b

# can also like
# for i in range(1, 4):
# print(i)

for i in range(1, a//b):
    print(i)

# print(a + b / 3 -4 * 12)
print(8 / 2 * 3)
print(8 * 3 / 2)
print((((a+b) / 3) - 4) * 12)


# declares a string
parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])  # print the 3rd position from the string
print(parrot[0])  # prints the first letter

print(parrot[-1])  # takes the 0 position back to the end
print(parrot[0:6])  # slices from 0-6 position

print(parrot[:6])  # slices automatically until the 6th position
print(parrot[6:]) # runs till the end
print(parrot[-4:-2])  #backwards characters moving forwards 

print(parrot[0:6:2]) #start at 0 - up to 6(not including) skip 2
print(parrot[0:6:3])  #start at 0 - up to 6(not including) skip 3


number = "9,223,372,036,854,775,807"
print(number[1::4]) #start at position1, skip 4

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3]) #extracts numbers only

#string concatonation 
string1 = "He's"
string2 = "probably"
print(string1 + string2)

# we can multiple and follow operador precedence
print("Hello " * 5)
print("Hello " * (5+4))
print("Hello " * 5 + "4")
today = "friday"

# we can find substrings automatically using "in" operador
print("day" in today) # true
print("fri" in today) #true
print("thur" in today) #false
print("parrot" in "fjord") #false

