def adding(func):
    def square(a,b):
        return func(a,b)**2
    return square
@adding
def display(a,b):
    return (a+1)*(b+1)

print(display(2,3))