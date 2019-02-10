
#set Math
math_students = {"Matthew", "Jose", 'Timmy', 'James', "Kyle", "Victoria", "James"}
biology_students = {"Jose", "Heather", 'John', 'Kyle', "James", "Sarah"}

#To generate a set with all unique students 
merge = math_students | set(biology_students) #combine both
print(merge)

# To generate a set with students who are in both courses
intersection_sample = math_students & set(biology_students)
print(intersection_sample) # Jose, James, Kyle