# show_args
# Write a function called show_args which accepts a function and returns another function. Before invoking the function passed to it,
# show_args should be responsible for printing two things: a tuple of the positional arguments, and a dictionary of the keyword arguments.

'''
@show_args
def do_nothing(*args, **kwargs):
    pass

do_nothing(1, 2, 3,a="hi",b="bye")

# Should print (on two lines):
# Here are the args: (1, 2, 3)
# Here are the kwargs: {"a": "hi", "b": "bye"}
'''

from functools import wraps


def show_args(fn):
    """Takes in do_nothing params to print """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """Prints the params """
        statement_1 = args
        statement_2 = kwargs
        # return statement_1, statement_2
        print('Here are the args: {}'.format(args))
        print(f'Here are the kwargs: {kwargs}')
        wrapper.__name__ = fn.__name__
        wrapper.__doc__ = fn.__doc__

    return wrapper

@show_args
def do_nothing(*args, **kwargs):
    """Can perform operations here as well as tying this to the the show_args """
    pass

# Test
print(do_nothing(1, 2, 3, a="hi", b="bye"))
print(do_nothing, do_nothing.__doc__)
print(show_args.__doc__)
help(show_args)