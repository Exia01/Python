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


loop_count = 3
answer = [[x for x in range(loop_count)] for i in range(loop_count)]
print(answer)

loop_count = 10
answer = [[x for x in range(loop_count)] for i in range(loop_count)]
print(answer)