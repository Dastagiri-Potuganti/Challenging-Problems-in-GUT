'''
11.Find the largest and  smallest digit in a number
Problem Statement
Given a number, find the largest and smallest digit using only loops.'''

number=int(input("Enter a number:"))
largest_number=float('-inf')
smallest_number=float('inf')
while number>0:
    digit=number%10
    if digit>largest_number:
        largest_number=digit
    if digit<smallest_number:
        smallest_number=digit
    number//=10

print("Larget Digit is",largest_number)
print("Smallest digit is",smallest_number)