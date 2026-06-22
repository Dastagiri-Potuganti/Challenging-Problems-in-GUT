n=int(input("Enter limit:"))
x=[]
for i in range(n):
    ch=int(input("Enter 0 or 1:"))
    x.append(ch)
count=0
y=0
for i in x:
    if i==0:
        count+=1
    else:
        y=count
        count=0
print(y)