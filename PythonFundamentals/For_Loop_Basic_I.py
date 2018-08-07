# Basic
for count in range(0, 151, 10):
    print(count)

# multiples of 5
for count in range(5, 1000000, 5):
    print(count)

# Counting the Dojo way
for i in range(1, 100):
    if i % 10 == 0:
        print('Dojo', i)
    elif i % 5 == 0:
        print('Coding', i)
    else:
        print(i)

# Whoa that sucker is huge
total = 0

for i in range(0, 500000, 1):
    if i % 2 != 0:
        total += i
print(total)

# Countdown by Fours
for i in range(2018, -2, -4):
    print(i)

# Flexible Countdown
for i in range(12, 1, -3):
    if i % 3 == 0:
        print(i)

