# write a function called "calculate"
# accepts a list of keyword arguments
# Make a float - a boolean which returens a float if true or an interger if false
# Operation - it is either 'add', 'subtract', 'multiply' or 'divide'
# First - is a number. Second, another number. Message which is a string that can be added.

'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''


def calculate(**kwargs):
    def operation_result(a=kwargs['first'], b=kwargs['second'],  operation=kwargs['operation']):
        state = 0
        if operation == "add":
            return a + b
        elif operation == "divide":
            return a / b
        elif operation == "multiply":
            return a * b
        return a - b

    default_message = "The result is "
    result = operation_result()
    if kwargs['make_float'] == False:
        result = int(result)

    try:
        if kwargs['message']:
            return "{} {}".format(kwargs['message'], result)
    except KeyError:
        return "{}{}".format(default_message, result)

# Test cases


print(calculate(make_float=True, operation='divide',
                first=3.5, second=5))  # "The result is 0.7"

print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4)) # "You just added 6"
print(calculate(make_float=True, operation='subtract', first=10, second=5.5)) # "The result is 4.5"

#Much Simple Way:

# write a function called "calculate"
# accepts a list of keyword arguments
# Make a float - a boolean which returens a float if true or an interger if false
# Operation - it is either 'add', 'subtract', 'multiply' or 'divide'
# First - is a number. Second, another number. Message which is a string that can be added.

'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''

def calculate_refractored(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final