def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
    
x=[11,12,13,14,15,16]
cnt=0
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if prime(x[i]+x[j]):
            cnt+=1
print(cnt)