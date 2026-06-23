x=list(map(int,input("Enter elements:").split(' ')))
k=2
k=k%len(x)
#right shift
print(x[-k:]+x[:-k])
#left shift
print(x[k:]+x[:k])
