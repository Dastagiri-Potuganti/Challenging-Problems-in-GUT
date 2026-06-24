x=[100,4,200,1,3,2]
count=0
for i in range(1,len(x)+1):
    if i in x:
        count+=1

print(count)