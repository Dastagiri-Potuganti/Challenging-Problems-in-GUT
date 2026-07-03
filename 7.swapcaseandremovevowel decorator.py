def swap(func):
    def inner(x):
        return (func(x)).swapcase()
    return inner

@swap
def display(n):
    x=''
    for i in n:
        if i not in ['a','e','i','o','u']:
            x+=i
    return x

print(display("Python"))