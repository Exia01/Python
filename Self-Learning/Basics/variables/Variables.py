# expressions are variables that are used to compute values.

greetings = "Jose"
_myName = "Sixto"
Sixto91 = "Great"
Sixto_Was_26 = "Hiii"
Greeting = "Yooo There"
print(Sixto_Was_26 + " " + greetings)

age = 24
print(age)

print(greetings + " " + _myName)

#integer are fasters than floats
a = 12
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# can implement in a loop but not as a float
# for i in range(1, 4):
    #print(i)

for i in range(1, a//b):
    print(i)

# print(a + b / 3 -4 * 12)
print(8 / 2 *3)
print(8 * 3 / 2)
# Operator precedence
print(a + b / 3 - 4 * 12)  # -35.0

# use parenthesis for explicit operation. 
print((((a+b) /3 ) -4) *12) # 12.0


