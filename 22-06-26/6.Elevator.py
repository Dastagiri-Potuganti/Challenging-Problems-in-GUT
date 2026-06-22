n=int(input('Enter number of floors:'))
for i in range(1,n+1):
    if i<=n+1//2:
        for j in range(1,i+1):
            print(j,end='')
        print()
    else:
        for j in range(n+1-i):
            print(j,end='')
        print()