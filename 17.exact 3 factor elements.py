def factors(n):
    cnt=2
    for i in range(2,n//2+1):
        if n%i==0:
            cnt+=1
        
    return cnt

x=[4,6,9,10,25,27]
y=[]
for i in x:
    if factors(i)==3:
        y.append(i)

print(y)