# Write a function called return_day. This function takes in one parameter; number from (1-7)
# It then returns the day of the week. --> Sunday is 1, Monday is 3 and so on

# Example using dictionary

exercises
def return_day(number=0):
    days = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday',
            4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
    day = days.get(number, None)
    if not day:
        return "No valid number provided. Numbers are 1-7"
    return day


print(return_day(0))

# Example using lists


def return_day_2(num):
    days = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0
        return days[num-1]
    return None


print(return_day_2(4))


# Example using Error Handling
print(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][-1])

def return_day_3(num):
    try:
        return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][num-1]
    except IndexError as e:
        # print(e) # prints out error
        return None

print(return_day_3(9))
