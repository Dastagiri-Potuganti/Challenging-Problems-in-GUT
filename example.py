num=15958
d='5'
def func(x):
    x=str(x)
    if d not in x:
        return '-1'
    ans=-1
    for i in range(len(x)):
        if x[i]==d:
            new_num = x[:i] + x[i+1:]
            if new_num == "":
                value = 0
            else:
                value = int(new_num)
            if value>ans:
                ans=value
    return ans

print(func(num))
               
        
        
    
