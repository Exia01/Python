# Let's define a speed_test decorator
from functools import wraps
from time import time

# This simplfies the code for speed test in iterators


def speed_test(fn):
    """Takes a generator and returns the total and timing"""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        results = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
    return wrapper


@speed_test
def sum_nums_gen():
    return sum(x for x in range(90000000))


@speed_test
def sum_nums_list():
    return sum([x for x in range(90000000)])


print(sum_nums_gen())
print(sum_nums_list())


""" In the wrapper function, we are adding the additional logic that decorates our function, and we are then instructing it to call the decorated function and return the function call results to the wrapper function which is ready to be executed at a later point.

Therefore, when the decorated function gets called, the wrapper function gets invoked with the passed *args and **kwargs, which are used to also call the decorated function and return its results from the wrapper directly (in addition to adding logic that decorates the function, like the print statements in this case).

By returning the wrapper function which is not invoked right away, we can call it any time we need later. """
