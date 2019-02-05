list_one = [1,2,3,4]
list_two = [3,4,5,6]
answer = [num for num in list_one if num in list_two]
print(answer)
names = ["Elie", "Tim", "Matt"]
answer2 = [word[::-1].lower() for word in names]
print(answer2)

numbers = [x for x in range(1,101)]
answer =  [num for num in numbers if num%12 == 0]
print(answer)