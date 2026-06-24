#a snake moves left-right in one row and right -left in next row
n=int(input("ENter number of rows:"))
for i in range(1,n+1):
    s='' 
    for j in range(1,i+1):
        s+=str(j)
    if i%2==0:
        print(s[::-1])
    else:
        print(s)