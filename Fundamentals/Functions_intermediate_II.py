# students = [
#     {"first_name":  "Michael", "last_name": "Jordan"},
#     {"first_name": "John", "last_name": "Rosales"},
#     {"first_name": "Mark", "last_name": "Guillen"},
#     {"first_name": "KB", "last_name": "Tonel"}
# ]
# # should output this
# # Michael Jordan
# # John Rosales
# # Mark Guillen
# # KB Tonel


# def printstudent():
#     for i in students:
#         print(i["first_name"], i["last_name"])


# printstudent()

users = {
    "Students": [
        {"first_name":  "Michael", "last_name": "Jordan"},
        {"first_name": "John", "last_name": "Rosales"},
        {"first_name": "Mark", "last_name": "Guillen"},
        {"first_name": "KB", "last_name": "Tonel"}
    ],
    "Instructors": [
        {"first_name": "Michael", "last_name": "Choi"},
        {"first_name": "Martin", "last_name": "Puryear"}
    ]
}

for i in users:
    print(i)
    for b in range(len(users[i])):
        # print(+ users[i][b]["first_name"] + " " + users[i][b]["last_name"])
        names = users[i][b]["first_name"] + "" + users[i][b]["last_name"]
        total = len(names)
        # print((len(names)))
        # print((len(users[i][b]["first_name"]), + b+1))
        # print((len(users[i][b]["first_name"]), + total))
        # print(b + 1, "-", names, "-", total)
        print(b+1, "-", names, "-",  total)
