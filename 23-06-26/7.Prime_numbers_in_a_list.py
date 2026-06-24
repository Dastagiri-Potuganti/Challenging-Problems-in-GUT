def prime(x):
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    else:
        return True
x=list(map(int,input("Enter inputs:").split(',')))
for i in x:
    if prime(i):
        print(i)