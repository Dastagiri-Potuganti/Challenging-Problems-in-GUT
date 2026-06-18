'''
6. Calculate Bill:
0-100 units->$2 per unit
101-200 units->$3 per unit
201+ units->$5 per unit'''

units=int(input("Enter number of units Consumed:"))
bill=0
'''if units<=100:
    print(units*2)
elif units<=200:
    print(units*3)
elif units>200:
    print(units*5)'''
if units<=100:
    print(units*2)
elif units>100 and units<=200:
    bill+=100*2
    bill+=(units-100)*3
    print(bill)
else:
    bill+=100*2
    bill+=100*3
    bill+=(units-200)*5
print(bill)