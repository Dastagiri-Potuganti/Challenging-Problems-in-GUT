x=(('a',1),('b',2),('c',3))
# y=dict(x)
y={}
# for i,j in x:
#     y[i]=j
for i in x:
    y[i[0]]=i[1]
print(y)