'''
4. A delivery partner earns:
$50 per delivery
Bonus $200 if deliveries>20
Calculate earnings.'''

deliveries=int(input("ENter number of deliveries:"))
if deliveries>20:
    print((deliveries*50)+200)
else:
    print(deliveries*50)