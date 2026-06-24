'''
5. Vehicles passing through a toll:
Bike=$20
Car=$50
bus=$100
Input vehicle types until"STOP".
Print total Collection.'''

collection=0
while True:
    vehicle=input("Enter type of vehilcle:")
    if vehicle =='stop':
        break
    else:
        if vehicle=='bike':
            collection+=20
        elif vehicle =='car':
            collection+=50
        elif vehicle =='bus':
            collection+=100
print("Total Collection is:",collection)