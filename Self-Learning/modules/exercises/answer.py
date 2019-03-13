# Built In Modules Exercise
#Import the math   module
#Use math.sqrt   to nd the square root of 15129 and save it to variable called

def answer(num):
    """ Will always return the sqrt of a number
    >>> answer(36)
    6.0
    >>> answer(90)
    9.486832980505138
    >>> answer(20)
    4.47213595499958

    >>> answer(None)
    Traceback (most recent call last):
    ...
    TypeError: must be real number, not NoneType
    """
    import math; answer = math.sqrt(num)
    return answer

# run py -m doctest -v doctest-demo2.py