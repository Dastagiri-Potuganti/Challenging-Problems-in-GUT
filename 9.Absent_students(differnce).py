all={'a','b','c','d','e'}
pre={'a','c','e'}
abs=set()
# print(all-pre)
for i in all:
    if i not in pre:
        abs.add(i)

print(abs)