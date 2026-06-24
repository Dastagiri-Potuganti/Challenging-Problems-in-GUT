'''
7. Input Motion values continuously.
Stop when 3 consecutive motion values are greater than 100.'''

count=0
while True:
    num=int(input("Enter a number:"))
    if num>100:
        count+=1
    else:
        count=0
    if count==3:
        print("Intruder Detected")
        break