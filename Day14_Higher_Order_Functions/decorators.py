# Normal function
def greeting():
    return "Welcome to Python"

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

g = uppercase_decorator(greeting)
print(g())

@uppercase_decorator
def greeting2():
    return "Welcome to Python"
print(greeting2())
