x=[1,4,45,6,10,8]
k=22
s=0
for i in range(len(x)):
    for j in range(i+1,len(x)-1):
        s=x[i]+x[j]
        a=s+x[j+1]
        if a==k:
            print(x[i],x[j],x[j+1])