# yes_or_no
# Write a function called yes_or_no, which returns a generator that rst yields yes  , then no  , then yes  , then no  , and so on.

def yes_or_no():
    response = ("yes", "no")
    count = 1
    state = response[0]
    while count < 5:
        yield state
        if state == "yes":
            state = "no"
        else:
            state = "yes"
        count+=1

for response in yes_or_no():
    print(response)