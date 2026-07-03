# def upper(func):
#     def inner(x):
#         return func(x).upper()
#     return inner

# @upper
# def reverse(x):
#     return x[::-1]

# print(reverse('python'))

class Decorator:
    def __init__(self,fun):
        self.func=fun
    def __call__(self):
        print('*'*10)
        self.func()
        print('*'*10)
@Decorator
def display():
    print("Hello")

display()
        