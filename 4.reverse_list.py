x=[1,2,3,4]
s=0
e=len(x)-1
while s<e:
    x[s],x[e]=x[e],x[s]
    s+=1
    e-=1

print(x)