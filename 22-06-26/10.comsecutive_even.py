n=int(input("Enter limit:"))
x=[]
for i in range(n):
    ch=int(input("Enter a number:"))
    x.append(ch)
count=0
for i in x:
    if count==3:
        print("Alert")
        break
    if i%2==0:
        count+=1
    else:
        count=0
    