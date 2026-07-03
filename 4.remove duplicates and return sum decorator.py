def removeduplicate(func):
    def add(x):
        a=func(x)
        b=[]
        for i in x:
            if i not in b:
                b.append(i)
        return sum(b)
    return add

@removeduplicate
def output(x):

    return x

print(output([1,2,2,3,3]))