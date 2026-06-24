n=int(input("Enter number of days:"))
sum=0
for i in range(n):
    temp=int(input("ENter today temperature:"))
    sum+=temp
print(sum/n)