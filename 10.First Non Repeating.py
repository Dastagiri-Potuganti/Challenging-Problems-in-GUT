x=[4,5,1,2,0,4,1,2]
y=[]
for i in x:
    if x.count(i)==1:
        y.append(i)
print(y[0])