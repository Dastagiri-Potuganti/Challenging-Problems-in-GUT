x=[1,2,3,2,4,1,5]
# y=set(x)
# print(y)
y=[]
for i in  x:
    if i not in y:
        y.append(i)
print(y)