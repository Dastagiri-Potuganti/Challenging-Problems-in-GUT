def palindrome(x):
    x=str(x)
    if x == x[::-1]:
        return True
    else:
        return False

def outer(func):
    def inner(x):
        a=func(x)
        if palindrome(a):
            return a**2
        else:
            return 'NOt a Palindrome'
    return inner

@outer
def display(x):
    return x
    
print(display(121))