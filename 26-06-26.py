#1.Count Frequency of each tuple
'''x=[(1,2),(3,4),(1,2),(5,6),(3,4),(3,4)]
y={}
for i in x:
    if i not in y:
        y[i]=1
    else:
        y[i]+=1
print(y)'''

#2.Find missing characters
'''a=set('abcdefghijklmnopqrstuvwxyz')
b=set('chatgpt')
print(a-b)'''

#3.Employee Attendence analyzer
'''attendance = [
    ("Nani","Mon"),("Rahul","Mon"),
    ("Nani","Tue"),("Sneha","Tue"),
    ("Rahul","Wed"),("Nani","Wed"),
    ("Sneha","Wed"),("Rahul","Thu"),
    ("Rahul","Fri")
]

employees = []
days = []

# Unique employees and days
for e, d in attendance:
    if e not in employees:
        employees.append(e)
    if d not in days:
        days.append(d)

# Total working days and highest attendance
highest = 0
top = []

print("Total working days:")
for e in employees:
    c = 0
    for x, y in attendance:
        if x == e:
            c += 1
    print(e, c)

    if c > highest:
        highest = c
        top = [e]
    elif c == highest:
        top.append(e)

print("\nHighest attendance:", top)

# Days on which every employee was present
print("\nDays all employees were present:")
for d in days:
    ok = True
    for e in employees:
        present = False
        for x, y in attendance:
            if x == e and y == d:
                present = True
                break
        if not present:
            ok = False
            break
    if ok:
        print(d)

# Employees absent on Friday
print("\nEmployees absent on Friday:")
for e in employees:
    present = False
    for x, y in attendance:
        if x == e and y == "Fri":
            present = True
            break
    if not present:
        print(e)'''

#4.Linbrary Book Borrowing System
'''borrowed = {"Alice":["Python","SQL","Python"],
	      "Bob":["Java","Python"],
   	      "Charlie":["SQL","C++","Java"],
	      "Diana":["Python","C++"]    }

students=[]
books=[]
books_count={}
max=0
max_students=[]
for x,y in borrowed.items():
    if x not in students:
        students.append(x)
    if type(y) is list:
        for j in y:
            if j not in books or  j not in books_count:
                books.append(j)
                books_count[j]=1
            else:
                books_count[j]+=1

    if len(y)>=max:
        max=len(y)
        max_students.append(x)
#1.
print("Unique Books Borrowed by all students:",books)
#2.
print("Count of each book was borrowed:",books_count)
#3.
print("Maximum Books Borrowed by:",max_students)
#4.
print("Books Borrowed by more than one student:")
for j,i in books_count.items():
    if (i)>1:
        print(j)'''


#5.University Count Enrollment
# courses = {"Python":{"Nani","Rahul","Anjali"},
# 	   "Java":{"Rahul","Sneha"},
# 	   "SQL":{"Nani","Sneha","Rahul"},
# 	   "React":{"Anjali","Nani"}   }
# language=[]
# students=[]
# max=0
# max_course=[]
# students_count={}
# for i,j in courses.items():
#     if i not in language:
#         language.append(i)
#     if type(j) is set:
#         for k in j:
#             if k not in students:
#                 students.append(k)
#     if len(j)>=max:
#         max=len(j)
#         max_course.append(i)
# #3.
# print("Maximum students enrolled in courses:",max_course)



#6.Greatest elements right to pivot element and smallest elements left to pivot element
'''x=[9,12,3,5,14,10,10]
pivot=10
small=[]
large=[]
equal=[]
for i in range(len(x)):
    if x[i]<pivot:
        small.append(x[i])
    elif x[i]==pivot:
        equal.append(x[i])
    else:
        large.append(x[i])
    
print(small+equal+large)'''

#7.Flattern Nested dictionary
'''student = {
    "id": 101,
    "details": {
        "name": "Nani",
        "marks": 90
    }
}

x = {}

for key in student:
    if type(student[key]) == dict:
        for k in student[key]:
            x[key + "." + k] = student[key][k]
    else:
        x[key] = student[key]

print(x)'''


#9.Keeping Even numbers after one position to each number
'''x=[2,5,8,7,10,9]
for i in range(len(x)-1):
    if x[i]%2==0:
     x[i],x[i+1]=x[i+1],x[i]
print(x)'''

#10.Replacing element with next greatest number
'''x=[16,17,4,3,5,2]
for i in range(len(x)-2):
    x[i]=max(x[i+1:])
else:
    x.append(-1)
print(x)'''


#11.Swapping first and last element in a tuple inside list

'''x=[(1,2,3),(4,5,6),(7,8,9)]
for i in range(len(x)):
    a=list(x[i])
    a[-1],a[0]=a[0],a[-1]
    x[i]=tuple(a)

print(x)'''
