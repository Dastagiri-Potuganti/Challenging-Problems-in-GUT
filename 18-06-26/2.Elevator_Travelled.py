'''  2. An elevator starts at floor().
Given N requests, print the total floors travelled.'''

current_floor =0
count=0
for i in range(int(input("Enter total number of floors do you want to travel:"))):
    next_floor=int(input("Enter floor number to travel:"))
    if next_floor>current_floor:
        count+=next_floor-current_floor
    else:
        count+=current_floor-next_floor
    current_floor=next_floor
print(count)