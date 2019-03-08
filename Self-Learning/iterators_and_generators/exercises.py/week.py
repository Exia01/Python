# Week Generator Exercise
# Write a function called week, which returns a generator that yields each day of the week, starting with Monday and ending with Sunday.
# After Sunday, the generator is exhausted.  It does not start over.

'''
days = week()
next(days) # 'Monday'
next(days) # 'Tuesday'
next(days) # 'Wednesday'
next(days) # 'Thursday'
next(days) # 'Friday'
next(days) # 'Saturday'
next(days) # 'Sunday'
next(days) # StopIteration
'''


def week():
    days = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Sunday',
    }
    count = 1
    while count in days:
        print(days.get(count, count))
        yield days.get(count)
        count += 1

test = week()
print(list(test))