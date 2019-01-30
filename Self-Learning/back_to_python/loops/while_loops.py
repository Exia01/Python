# Continues to ask for user input until the user types 'bananas'
print("whats the secret password?")
msg = input()
while msg != "bananas":
	print("WRONG!")
	print('whats the secret password?')
	msg = input()
print("CORRECT!")


# for num in range(1,11):
# 	print(num)

# equivalent of above for loop
num = 1
while num < 11:
	print(num)
	num += 1
