def multiply(f):
    def multiple(a,b):
        return f(a,b)*2
    return multiple

@multiply
def add(a,b):
    return a+b

a=5
b=3
print(add(a,b))