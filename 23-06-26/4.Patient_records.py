def Patient(n):
    x=set(n)
    return x
def searching(n,s):
    for i in n:
        if i ==s:
            return True
        else:
            return False
a=list(map(int,input("Enter Patient Id:").split(' ')))
s=100
print("UniquePatients:",list(Patient(a)))
print("Unique Patient Count:",len(Patient(a)))
print("Patient Exist:",searching(Patient(a),s))