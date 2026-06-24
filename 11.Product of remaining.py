x=[1,2,3,4]
y=[]
for i in x:
    s=1
    for j in x:
        if i!=j:
            s*=j
    y.append(s)

print(y)