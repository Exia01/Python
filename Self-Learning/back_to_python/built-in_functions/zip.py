
# Zip makes an iterator that aggregates elements for each of the iterables
# Returns an iterator of tuples, where the ith tuple contains the i-th element from each of the argument sequences or iterables
# The iterator stops when the shortest input iterable is exhausted


nums1 = [1,3,45,2,43]
nums2 = [1, 2, 43]
print(list(zip(nums1, nums2))) # stops short
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']


# returns dict with {student:highest score} USING LIST COMP
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}
#(dan, 80, 98) #then creating a dictionary 
print(final_grades)


# returns dict with {student:highest score} USING MAP+LAMBDA
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
        )
    )
)
print(final_grades)
#(98,80) take the max and zip it with students(dan,98) --> then create a dictionary

# returns dict with student:average score
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
avg_grades = dict(
    zip(
        students,
        map(
            lambda pair: ((pair[0]+pair[1])/2),
            zip(midterms, finals)
        )
    )
)



#more optimized way of doing this. 

r = dict(zip(students, midterms))
print(r)

r = {item[0]: max(item[1], item[2]) for item in zip(students,midterms, finals)}
print(r)

r = {item[0]: round((item[1] + item[2])/2) for item in zip(students,midterms, finals)}
print(r)


# z = zip(
# 	students,
# 	map(
# 		lambda pair: max(pair),
# 		zip(midterms, finals)
# 	)
# )



#last example 
five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*five_by_two)))