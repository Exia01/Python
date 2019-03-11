# ensure_authorized
# Write a function called ensure_authorized which accepts a function and returns another function. The function passed to it should only
# be invoked if there exists a keyword argument with a name of "role" and a value of "admin". Otherwise, the inner function should return
# "Unauthorized"


from functools import wraps


def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(fn.__name__)
        if(any(v is "admin" for k,v in kwargs.items())):
            return fn(*args, **kwargs)
        else:
            return("Unauthorized")
    return wrapper


@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

@ensure_authorized
def show_test(*args, **kwargs):
    return "This is not a test"


# Test Cases

print(show_secrets(role="admin"))  # "Shh! Don't tell anybody!"
print(show_secrets(role="nobody"))  # "Unauthorized"
print(show_secrets(a="b"))  # "Unauthorized"


#more optimized way of doing things
def _ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper