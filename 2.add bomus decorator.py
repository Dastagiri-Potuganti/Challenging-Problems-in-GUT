def bonus(func):
    def add(x):
        return func(x)+100
    return add


@bonus
def display(x):
    return x


print(display(5000))