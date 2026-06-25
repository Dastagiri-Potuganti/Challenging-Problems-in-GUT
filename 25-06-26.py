#program 1
'''students={
    "Rahul":78,
    "Nani":95,
    "Anjali":88,
    "Vijay":67
    }
max_marks=float('-inf')
min_marks=float('inf')
s=0
total=len(students)
for m in students.values():
    s=s+m
    avg_marks=s/total
    if m>max_marks:
        max_marks=m
    if m<min_marks:
        min_marks=m
print('Highest Score:',max_marks)
print('Lowest Scorer:',min_marks)
print('Average Marks:',avg_marks)'''
#program 2
'''sentence='python is easy python is powerful'
output={}
for s in sentence.split():
    output[s]=sentence.count(s)
print(output)'''
#program 3
'''student={'A':101,'B':102,'C':103}
output={v:k for k,v in student.items()}
print(output)'''
#program 4
'''keys=['name','age','city']
values=['rahul',22,'hyderabad']
output={k:v for k,v in zip(keys,values)}
print(output)'''
#another way
'''keys=['name','age','city']
values=['rahul',22,'hyderabad']
output=dict(zip(keys,values))
print(output)'''
#program 5 based on values
'''marks={
    'rahul':78,
    'anjali':95,
    'sneha':88,
    'vijay':70
    }
sorted_list=sorted(marks.items(),key=lambda x:x[1])
print(sorted_list)'''
#another way based on keys
'''marks={
    'rahul':78,
    'anjali':95,
    'sneha':88,
    'vijay':70
    }
sorted_list=sorted(marks.items(),key=lambda x:x[0])
print(sorted_list)'''
#program 6
'''data={
    'A':10,
    'B':20,
    'C':10,
    'D':30,
    'E':20
    }
freq={}
for v in data.values():
    freq[v]=freq.get(v,0)+1
duplicates=[]
for k,v in freq.items():
    if v>1:
        duplicates.append(k)
print(duplicates)'''
#program 7
'''words=['apple','ant','ball','bat','cat','car']
output={}
for word in words:
    first=word[0]
    if first in output:
        output[first].append(word)
    else:
        output[first]=[word]
print(output)'''
#program 8
'''students={
    'A':80,
    'B':88,
    'C':91,
    'E':75
    }
first=float('-inf')
second=float('-inf')
for m in students.values():
    if m>first:
        first=m
        second=first
    if m>second and m<first:
        second=m
print(second)'''
#program 9
'''d1={
    'A':10,
    'B':20,
    'C':30
    }
d2={
    'B':15,
    'C':25,
    'D':40
    }
for k,v in d2.items():
    if k in d1:
        d1[k]=d1[k]+v
    else:
        d1[k]=v
print(d1)'''
#program 10
'''students={
    'ram':95,
    'rahul':82,
    'kiran':74,
    'anjali':65,
    'vijay':45
    }
output={}
for n,m in students.items():
    if m>90:
        output[n]='A'
    elif m>80:
        output[n]='B'
    elif m>70:
        output[n]='C'
    elif m>60:
        output[n]='D'
    elif m>50:
        output[n]='E'
    else:
        output[n]='F'
print(output)'''
#program 11
'''data={
    'A':10,
    'B':20,
    'C':10,
    'D':20
    }
output={}
for n,v in data.items():
    if v in output:
        output[v].append(n)
    else:
        output[v]=[n]
print(output)'''
#program 12
'''day1 = {'ram':1,'rahul':1,'anjali':1}
day2 = {'rahul':1,'kiran':1,'ram':1}
output = day1.copy()
for n, v in day2.items():
    if n in output:
        output[n] += v
    else:
        output[n] = v
print(output)'''
