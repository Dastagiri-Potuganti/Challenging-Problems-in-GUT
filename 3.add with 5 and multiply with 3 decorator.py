def multiply(func):
    def wrapper(a,b):
        return func(a,b)*3
    return wrapper



def add(func):
    def wrapper(a,b):
        return func(a,b)+5
    return wrapper
@multiply
@add
def display(a,b):
    return a+b

print(display(4,2))