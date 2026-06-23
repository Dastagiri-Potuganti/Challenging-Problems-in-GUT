user_names=[]
duplicate_users=[]
while True:
    user=input("Enter user name:")
    if user not in user_names:
        user_names.append(user)
    else:
        if user not in duplicate_users:
            duplicate_users.append(user)
    ch=input("Do you want to add another user(yes/no):")
    if ch== 'no':
        break
print("Duplicate logins:",duplicate_users)
print("Unique Users count:",len(user_names))
print("User logged more than once:",duplicate_users)