# we can write test for function inside the docstring
# write code that looks like it's inside of a REPL

# Example1




def double(values):
    """ double the values in a list
    >>> double([1,2,3,4])
    [2, 4, 6, 8]

    >>> double([2,4,10,18])
    [4, 8, 20, 36]

    >>> double([])
    []
    >>> double(['a','b','c'])
    ['aa', 'bb', 'cc']

    >>> double([True, None])
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

    """

    new_list = (2*v for v in values)
    return  list(new_list)


# to run python3 -m doctest -v doctest-demo2.py


#problems that come when it comes with this
def say_hi():
    """ 
    >>> say_hi()
    "hi"
    """
    return "hi"  #fails because it expects single quotes
    
def true_that():
    """ 
    >>> true_that()
    True 
    """
    return True #magic whitespace after True 