from random import choice


def eat(food, is_healthy):
    start = "I'm eating "
    state = " because YOLO"

    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy must be a boolean")


    if food and is_healthy:
        state = " because my body is a temple"
        return f'{start}{food},{state}'
    elif food and not is_healthy:
        return f'{start}{food},{state}'
    

def nap(num_hours):
    if num_hours >= 2:
        return f"Ugh I overslept. I didn't mean to nap for {num_hours} hours!"
    return f"I'm feeling refreshed after my {num_hours} hour nap"


def is_funny(person):
    if person is "Tim":
        return False
    return True


def laugh():
    laughs = ('lol', 'haha', 'tehehe')
    return(choice(laughs))

# we can leave these empty and perform the test in another file -> tests.py
