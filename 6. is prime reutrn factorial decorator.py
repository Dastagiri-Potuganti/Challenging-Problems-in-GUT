def prime(n):
    for d in range(2,n//2+1):
        if n%d==0:
            return False
    return True
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

def isprifact(n):
    def inner(x):
        a= n(x)
        if prime(a):
            return fact(a)
        else:
            return 'Not Prime'
    return inner
        
@isprifact        
def display(n):
    return n

print(display(5))