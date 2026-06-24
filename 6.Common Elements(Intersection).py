a={1,2,3,4}
b={3,4,5,6}
# print(a&b)
c=set()
for i in a:
    if i in b:
        c.add(i)
print(c)