''' A parking lot records vehicles entering and exiting.
Input N events:
"In"->vehicle entered
"Out"->vehicle exited
print the maximum vehicles present at any time. '''



in_cnt=0
out_cnt=0
for i in range(int(input("Enter total number of inputs:"))):
    ch=input("Enter 'IN' or 'OUT' :")
    if ch == 'in':
        in_cnt+=1
    else:
        out_cnt+=1

print("vehicles Present are:",in_cnt-out_cnt)