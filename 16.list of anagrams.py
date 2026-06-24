def anagram(n):
    cnt=len(str(n))
    s=0
    temp=n
    while n>0:
        d=n%10
        s+=d**cnt
        n//=10
    if temp == s:
        return True
    else:
        return False
x=[153,370,123,407,100]
y=[]
for i in x:
    if anagram(i):
        y.append(i)
print(y)