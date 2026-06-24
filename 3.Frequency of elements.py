x=[1,2,2,3,1,2]
y={}
for i in x:
    if i in y:
        y[i]+=1
    else:
        y[i]=1
print(y)

# for i,j in y.items():
#     print(f"{i}:{j}")