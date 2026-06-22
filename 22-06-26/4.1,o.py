n=int(input("Enter number of rows:"))
for i in range(n+1):
    if i%2==0:
        print('0'*i)
    else:
        print('1'*i)