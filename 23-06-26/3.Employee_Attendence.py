unique_employees=[]
dup_empl=[]
count=0
while True:
    employee_number=int(input("Enter your employee_number:"))
    if employee_number not in unique_employees:
        unique_employees.append(employee_number)
    else:
        if employee_number not in dup_empl:
            dup_empl.append(employee_number)
    count+=1
    ch=input("Do you want to add another employee entry(yes/no):")
    if ch =='no':
        break
print("Total Entries:",count)
print('Duplicate Employee IDs:',dup_empl)
print("Unique Employess:",unique_employees)