'''
10.Write a Python program to find the minimum number among n numbers entered by the user using only loops?'''
minimum_number=float('+inf')
iteration=int(input("How many numbers do you want to input:"))
while iteration > 0:
    number=int(input("Enter a number:"))
    if number<minimum_number:
        minimum_number=number
    iteration-=1

print(minimum_number)