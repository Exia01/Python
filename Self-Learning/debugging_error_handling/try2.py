# try:
# except:
# else:
# finally:


while True: #always runs
	try:
		num = int(input("please enter a number: "))
	except ValueError: #value since we need a number
		print("That's not a number!")
	else: # execute logic if passing the try
		print("Good job, you entered a number!")
		break
	finally: #not as commonly used. 
		print("RUNS NO MATTER WHAT!")
print("REST OF GAME LOGIC RUNS!") # outside of the whileloop

# try:
# 	num = int(input("please enter a number: "))
# except:
# 	print("That's not a number!")
# else:
# 	print("I'M IN THE ELSE!")
# finally:
# 	print("RUNS NO MATTER WHAT!")

