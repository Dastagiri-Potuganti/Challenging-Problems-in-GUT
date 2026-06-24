IP=[]
dup_ip=[]
while True:
    ip=input("Enter an IP Address:")
    if ip not in IP:
        IP.append(ip)
    else:
        dup_ip.append(ip)
    ch=input("Do you want to add another ip address(yes/no):")
    if ch=='no':
        break
print("Duplicate IP's are:",list(set(dup_ip)))
print("Unique IP Count:",len(IP))
for i in dup_ip:
    if dup_ip.count(i)==3:
        print("Suspicious IP's:",i)
        break
