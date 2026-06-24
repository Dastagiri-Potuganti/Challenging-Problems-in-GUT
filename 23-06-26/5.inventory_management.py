inventory={}
while True:
    item=input("Enter an item name:")
    if item not in list(inventory.values()):
        qty=int(input("Enter quantity of this product:"))
        inventory.update({
            'name':item,
            'quantity':qty
        })
    else:
        print("Item already exists")
    ch=input("Do you want to add another item(yes/no):")
    if ch =='no':
        break
max=0
max_product=''
s=0
# print("Out of Stock Products:",end='')
# for i in list(inventory.values()):
#     if i[1]==0:
#         print(i[0],end='')
#     if i[1]>max:
#         max=i[1]
#         max_product=i[0]
#     s+=i[1]

# print('Maximum Stock Product:',max_product)
# print("Total Inventory:",s)
print(inventory.values())