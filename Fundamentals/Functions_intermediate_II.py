# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]
# # should output this
# # Michael Jordan
# # John Rosales
# # Mark Guillen
# # KB Tonel


# def printstudent():
#     for i in students:
#         print(i['first_name'], i['last_name'])


# printstudent()

users = {
    'Students': [
        {'first_name':  'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'Instructors': [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': 'Puryear'}
    ]
}

for i in users:
    # print(i)
    # print(len(users[i]))
    for j in range(len(users[i])):
        print(users[i][j]['first_name'] + ' ' + users[i][j]['last_name'])

    # for j in range(len(users[i])):
    #     name = users[i][j]['first_name'] + ' ' + users[i][j]['last_name']
    #     leng = len(name)
    #     print((len(name)))
        # print(j + 1, '-', name, '-', leng)
