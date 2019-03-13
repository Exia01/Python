# we can write test for function inside the docstring
# write code that looks like it's inside of a REPL

# Example1


def add(x, y):
    """ add together x and y
    >>> add(2,3)
    5
    >>> add(1,2)
    3
    >>> add(100,200)
    300

    >>> add(8, "hi")
    Traceback(most recent call last):
            ...
    TypeError: unsupported operand types(s) for +: 'int' and 'str'
    """
    return x+y


# to run python3 -m doctest -v doctest-demo.py

# 1 items had no tests:
#     doctest-demo
# **********************************************************************
# 1 items had failures:
#    1 of   4 in doctest-demo.add
# 4 tests in 2 items.
# 3 passed and 1 failed.
# ***Test Failed*** 1 failures.