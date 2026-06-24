x=[-1,0,1,2,-1,-4]
y=[]
t=0
for i in range(len(x)):
    s=0
    for j in range(i+1,len(x)-1):
        s=x[i]+x[j]
        a=s+x[j+1]
        if a==t:
            y.append([x[i],x[j],x[j+1]])

print(y)