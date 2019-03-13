def eat(food, is_healthy):
    start = "I'm eating "
    state = " because YOLO"

    if food and is_healthy:
        state = " because my body is a temple"
        return f'{start}{food},{state}'
    elif food and not is_healthy:
        return f'{start}{food},{state}'
    return "I'm not really hungry"

def nap(num_hours):
    if num_hours >= 2:
        return f"Ugh I overslept. I didn't mean to nap for {num_hours} hours!"
    return f"I'm feeling refreshed after my {num_hours} hour nap"

# we can leave these empty and perform the test in another file -> tests.py
