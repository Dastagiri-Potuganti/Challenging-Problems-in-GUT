def composite(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return True
        
x=[2,4,5,6,8,11,15]
s=0
for i in x:
    if composite(i):
        s+=i
print(s)