'''
9. Battery starts at100%.
Each app usage reduces battery by given percentage.
stop when battery becomes less than 10%.
Print the session at which battery became critical.'''

battery_percentage=100
count=0
while True:
    battery_consumed=int(input("Enter the battery consumed in numbers:"))
    battery_percentage-=battery_consumed
    count+=1
    if battery_percentage<10:
        print("critical Session at ",count)
        break