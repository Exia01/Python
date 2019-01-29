Question1 = "How many kilometers did you walk today?"

print(Question1)
kms = input() #takes in a string

miles = float(kms) / 1.60934  # could apply the conversion at the input as well
miles = round(miles,2)
print(f'Your {kms} means, you walked a total of {miles} miles')